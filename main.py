# This Python file uses the following encoding: utf-8
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
#  pyuic5 form.ui -o ui_form.py
import sys
import traceback
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog
from PySide6.QtCore import QThread, Signal
import numpy as np
from src.camera import FlirCamera
from src.windows.Serial_popup import Serial_popup
from src.ui_form import Ui_MainWindow
from src.windows.customwindows import ConfigDialog, ProgressDialog

class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # self.ui = Ui_Main()
        self.setupUi(self)
        # self.retranslateUi(self)
        self.c = None
        self.capture_thread = None
        self.num_averages = 1
        self.actionConnect.triggered.connect(self.connect_serial)
        self.actionDisconnect.triggered.connect(self.disconnect_serial)
        self.actionLiveView.triggered.connect(self.liveview)
        self.action_Capture.triggered.connect(self.capture)
        self.actionConfig.triggered.connect(self.open_config_dialog)
    
    def connect_serial(self):
        dlg = Serial_popup()
        if dlg.exec():
            serial_number = dlg.get_results()
            self.c = FlirCamera(serial=int(serial_number))
            self.c.connect()
            dlg = QMessageBox()
            dlg.setWindowTitle("info!")
            dlg.setText("You have connected to the camera")
            button = dlg.exec()

            if button == QMessageBox.Ok:
                print("OK!")
    
    def disconnect_serial(self):
        if self.c:
            self.c.disconnect()
            self.c = None
            dlg = QMessageBox()
            dlg.setWindowTitle("info!")
            dlg.setText("You have disconnected from the camera")
            button = dlg.exec()

            if button == QMessageBox.Ok:
                print("OK!")
        else:
            dlg = QMessageBox()
            dlg.setWindowTitle("info!")
            dlg.setText("Please connect to camera first!!")
            button = dlg.exec()

            if button == QMessageBox.Ok:
                print("OK!")

    def liveview(self, checked):
        if checked:
            if self.capture_thread is None or not self.capture_thread.isRunning():
                self.capture_thread = CaptureThread(self.c.cam, self.num_averages)
                self.capture_thread.update_image.connect(self.update_plot)
                self.capture_thread.start()
        else:
            if self.capture_thread and self.capture_thread.isRunning():
                self.capture_thread.stop()
    
    def update_plot(self, img_averaged):
        self.GraphWidget.clear()
        self.GraphWidget.plot(img_averaged, pen='b', penWidth=0.1, symbol='o',
                              symbolSize=0.4, symbolPen='b')
    
    def capture(self):
        img_averaged = None
        # Create and show the progress dialog
        progress_dialog = ProgressDialog(self)
        progress_dialog.reset_progress(self.num_averages)  # Reset the progress bar with the maximum value
        progress_dialog.show()  # Show the progress dialog
        self.c.cam.start_capture()
        try:
            for i in range(0, self.num_averages):
                self.c.cam.read_next_image()
                image = self.c.cam.get_current_image()  # last image
                img_np = np.frombuffer(image['buffer'], dtype=np.uint16).reshape((image['rows'], image['cols']))
                if i == 0:
                    img_averaged = img_np.mean(axis=0)
                else:
                    img_averaged += img_np.mean(axis=0)
                progress_dialog.set_progress(i + 1)  # Increment progress
                # Process events to ensure the dialog remains responsive
                QApplication.processEvents()
            self.c.cam.stop_capture()
            if img_averaged is not None:
                img_averaged = img_averaged/(self.num_averages)
            self.GraphWidget.clear()
            self.GraphWidget.plot(img_averaged, pen='b', penWidth=0.1, symbol='o',
                        symbolSize=0.4, symbolPen='b')
            print("capture image success")
        except:
            print(f"failed to capture image {traceback.format_exc()}")
            self.c.cam.stop_capture()
        progress_dialog.close()

    def open_config_dialog(self):
        # Open the config dialog to get the number of averages
        dialog = ConfigDialog(self)
        if dialog.exec() == QDialog.Accepted:
            self.num_averages = dialog.get_averages()
            self.update_cam_settings(dialog.get_integration_time(), dialog.get_gain())
            print(f"Number of averages set to: {self.num_averages}")

    def update_cam_settings(self, IT, GAIN):
        self.c.cam.set_cam_abs_setting_value("shutter", IT)
        self.c.cam.set_cam_abs_setting_value("gain", GAIN)

class CaptureThread(QThread):
    # Custom signal to send data to the main thread
    update_image = Signal(np.ndarray)

    def __init__(self, cam, num_averages):
        super().__init__()
        self.cam = cam
        self._is_running = True
        self.num_averages = num_averages

    def run(self):
        while self._is_running:
            img_averaged = None
            print("start the live view")
            self.cam.start_capture()
            try:
                for i in range(0, self.num_averages):  # Modify loop size if necessary
                    self.cam.read_next_image()
                    image = self.cam.get_current_image()  # last image
                    img_np = np.frombuffer(image['buffer'], dtype=np.uint16).reshape((image['rows'], image['cols']))
                    if i == 0:
                        img_averaged = img_np.mean(axis=0)
                    else:
                        img_averaged += img_np.mean(axis=0)

                img_averaged = img_averaged / (self.num_averages)
                self.update_image.emit(img_averaged)  # Emit the result to update the GUI
            except:
                print(f"Failed to capture image {traceback.format_exc()}")
            finally:
                self.cam.stop_capture()
                print("end the live view")
        self.GraphWidget.clear()

    def stop(self):
        self._is_running = False
        self.quit()
        self.wait()
        self.GraphWidget.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Main()
    widget.show()
    sys.exit(app.exec())

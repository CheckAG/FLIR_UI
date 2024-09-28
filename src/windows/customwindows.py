from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QSpinBox, QDialogButtonBox, QSlider, QProgressBar
from PySide6.QtCore import Qt

class ConfigDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Configure settings for camera")
        self.setModal(True)

        # Create a layout
        layout = QVBoxLayout()

        # Label and SpinBox for the number of averages
        self.label_avg = QLabel("Set Number of Averages:", self)
        self.spin_box_avg = QSpinBox(self)
        self.spin_box_avg.setMinimum(1)  # Min value for averages
        self.spin_box_avg.setMaximum(100)  # Set a reasonable max value
        self.spin_box_avg.setValue(1)  # Default value

        # Label and slider for intergration time 
        self.label_integrationtime = QLabel("set integration time (in seconds):", self)
        self.slider_integrationtime = QSlider(self)
        self.slider_integrationtime.setOrientation(Qt.Horizontal)  # Horizontal slider
        self.slider_integrationtime.setMinimum(self.parent().c.cam.get_cam_abs_setting_range("shutter")[0])  # Minimum value for averages
        self.slider_integrationtime.setMaximum(self.parent().c.cam.get_cam_abs_setting_range("shutter")[1])  # Set a reasonable max value
        self.slider_integrationtime.setValue(self.parent().c.cam.get_cam_abs_setting_value("shutter"))  # Default value
        self.slider_integrationtime.setTickPosition(QSlider.TicksBelow)
        self.slider_integrationtime.setTickInterval(1)
        self.label_integrationtime_show = QLabel(f"{self.slider_integrationtime.value()}", self)
        self.slider_integrationtime.valueChanged.connect(self.update_slider_integrationtime)

        # Label and slider for gain
        self.label_gain = QLabel("set gain:", self)
        self.slider_gain = QSlider(self)
        self.slider_gain.setOrientation(Qt.Horizontal)  # Horizontal slider
        self.slider_gain.setMinimum(self.parent().c.cam.get_cam_abs_setting_range("gain")[0])  # Minimum value for averages
        self.slider_gain.setMaximum(self.parent().c.cam.get_cam_abs_setting_range("gain")[1])  # Set a reasonable max value
        self.slider_gain.setValue(self.parent().c.cam.get_cam_abs_setting_value("gain"))  # Default value
        self.slider_gain.setTickPosition(QSlider.TicksBelow)
        self.slider_gain.setTickInterval(1)
        self.label_gain_show = QLabel(f"{self.slider_gain.value()}", self)
        self.slider_gain.valueChanged.connect(self.update_slider_gain)

        # Buttons for OK and Cancel
        self.button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)

        # Add widgets to layout
        layout.addWidget(self.label_avg)
        layout.addWidget(self.spin_box_avg)
        layout.addWidget(self.label_integrationtime)
        layout.addWidget(self.slider_integrationtime)
        layout.addWidget(self.label_integrationtime_show)
        layout.addWidget(self.label_gain)
        layout.addWidget(self.slider_gain)
        layout.addWidget(self.label_gain_show)

        layout.addWidget(self.button_box)

        # Set layout to the dialog
        self.setLayout(layout)

    def update_slider_integrationtime(self):
        # Update the label text and position
        self.label_integrationtime_show.setText(f"{self.slider_integrationtime.value()}")
        slider_pos = self.slider_integrationtime.sliderPosition()
        # Position label above the slider handle
        self.label_integrationtime_show.move(self.slider_integrationtime.x() + slider_pos - (self.slider_integrationtime.width() // 2), 
                               self.slider_integrationtime.y() - self.slider_integrationtime.height() - 5)

    def update_slider_gain(self):
        # Update the label text and position
        self.label_gain_show.setText(f"{self.slider_gain.value()}")
        slider_pos = self.slider_gain.sliderPosition()
        # Position label above the slider handle
        self.label_gain_show.move(self.slider_gain.x() + slider_pos - (self.slider_gain.width() // 2), 
                               self.slider_gain.y() - self.slider_gain.height() - 5)

    def get_averages(self):
        # Return the value from the SpinBox
        return self.spin_box_avg.value()
    
    def get_integration_time(self):
        return self.slider_integrationtime.value()
    
    def get_gain(self):
        return self.slider_gain.value()

class ProgressDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Progress")
        self.setModal(True)
        layout = QVBoxLayout()
        # Progress bar for averaging
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setValue(0)
        # Label for progress information
        self.progress_label = QLabel("Processing...", self)
        layout.addWidget(self.progress_label)
        layout.addWidget(self.progress_bar)
        self.setLayout(layout)

    def set_progress(self, value):
        # Update the progress bar value
        self.progress_bar.setValue(value)

    def reset_progress(self, max_value):
        self.progress_bar.setMaximum(max_value)
        self.progress_bar.setValue(0)
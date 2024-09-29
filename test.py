import sys
from PySide6.QtWidgets import (
    QApplication, QDialog, QVBoxLayout, QHBoxLayout, QLabel, QSlider, QSpinBox, QCheckBox, QPushButton, QComboBox, QLineEdit, QFileDialog
)
from PySide6.QtCore import Qt

class CustomDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Configuration Panel")

        # Main Layout
        main_layout = QVBoxLayout()

        # === Acquisition Properties ===
        acquisition_layout = QVBoxLayout()
        acquisition_layout.addWidget(QLabel("Acquisition Properties"))

        # Exposure
        exposure_layout = QHBoxLayout()
        exposure_layout.addWidget(QLabel("Exposure:"))
        self.exposure_slider = QSlider(Qt.Horizontal)
        self.exposure_slider.setRange(0, 5000)
        self.exposure_slider.setValue(1000)
        self.exposure_label = QLabel("1000 ms")
        exposure_layout.addWidget(self.exposure_slider)
        exposure_layout.addWidget(self.exposure_label)
        acquisition_layout.addLayout(exposure_layout)

        # Gain
        gain_layout = QHBoxLayout()
        gain_layout.addWidget(QLabel("Gain:"))
        self.gain_slider = QSlider(Qt.Horizontal)
        self.gain_slider.setRange(0, 100)
        self.gain_slider.setValue(0)
        self.gain_label = QLabel("0.0 dB")
        gain_layout.addWidget(self.gain_slider)
        gain_layout.addWidget(self.gain_label)
        acquisition_layout.addLayout(gain_layout)

        # ROI
        roi_layout = QHBoxLayout()
        roi_layout.addWidget(QLabel("ROI:"))
        self.roi_slider = QSlider(Qt.Horizontal)
        self.roi_slider.setRange(0, 500)
        self.roi_slider.setValue(128)
        self.roi_label = QLabel("128 px")
        roi_layout.addWidget(self.roi_slider)
        roi_layout.addWidget(self.roi_label)
        acquisition_layout.addLayout(roi_layout)

        # Number of Averages
        avg_layout = QHBoxLayout()
        avg_layout.addWidget(QLabel("Num Avg.:"))
        self.avg_slider = QSlider(Qt.Horizontal)
        self.avg_slider.setRange(1, 100)
        self.avg_slider.setValue(1)
        self.avg_label = QLabel("1")
        avg_layout.addWidget(self.avg_slider)
        avg_layout.addWidget(self.avg_label)
        acquisition_layout.addLayout(avg_layout)

        # Median Filtering
        self.median_filter_checkbox = QCheckBox("Enable Median Filtering")
        acquisition_layout.addWidget(self.median_filter_checkbox)

        main_layout.addLayout(acquisition_layout)

        # === Logging Section ===
        logging_layout = QVBoxLayout()
        logging_layout.addWidget(QLabel("Logging"))

        self.log_checkbox = QCheckBox("Automatically log acquired spectra on disk")
        logging_layout.addWidget(self.log_checkbox)

        self.file_line_edit = QLineEdit()
        self.file_browse_button = QPushButton("Browse")
        file_layout = QHBoxLayout()
        file_layout.addWidget(self.file_line_edit)
        file_layout.addWidget(self.file_browse_button)
        logging_layout.addLayout(file_layout)

        self.combo_box = QComboBox()
        self.combo_box.addItems(["Comma Separated (.csv)", "Tab Separated (.tsv)"])
        logging_layout.addWidget(self.combo_box)

        main_layout.addLayout(logging_layout)

        # === Plot Settings ===
        plot_layout = QVBoxLayout()
        plot_layout.addWidget(QLabel("Plot Settings"))

        # Boxcar Smoothing
        boxcar_layout = QHBoxLayout()
        boxcar_layout.addWidget(QLabel("Boxcar Smoothing:"))
        self.boxcar_slider = QSlider(Qt.Horizontal)
        self.boxcar_slider.setRange(1, 10)
        self.boxcar_slider.setValue(3)
        self.boxcar_label = QLabel("3")
        boxcar_layout.addWidget(self.boxcar_slider)
        boxcar_layout.addWidget(self.boxcar_label)
        plot_layout.addLayout(boxcar_layout)

        # ComboBox for Plot Axis
        self.plot_axis_combo = QComboBox()
        self.plot_axis_combo.addItems(["Wavelengths", "Pixels", "Other"])
        plot_layout.addWidget(self.plot_axis_combo)

        # Raman Wavelength Slider
        raman_layout = QHBoxLayout()
        raman_layout.addWidget(QLabel("Raman Wavelength:"))
        self.raman_slider = QSlider(Qt.Horizontal)
        self.raman_slider.setRange(400, 1000)
        self.raman_slider.setValue(532)
        self.raman_label = QLabel("532.0 nm")
        raman_layout.addWidget(self.raman_slider)
        raman_layout.addWidget(self.raman_label)
        plot_layout.addLayout(raman_layout)

        # Checkboxes for plot settings
        self.blank_removal_checkbox = QCheckBox("Enable Blank Removal")
        self.baseline_removal_checkbox = QCheckBox("Enable Baseline Removal (Schulze et al.)")
        self.sgolay_checkbox = QCheckBox("Enable Savitzky-Golay Filtering (post process)")
        plot_layout.addWidget(self.blank_removal_checkbox)
        plot_layout.addWidget(self.baseline_removal_checkbox)
        plot_layout.addWidget(self.sgolay_checkbox)

        # Savitzky-Golay settings
        sg_layout = QHBoxLayout()
        sg_layout.addWidget(QLabel("Window size:"))
        self.sg_slider = QSlider(Qt.Horizontal)
        self.sg_slider.setRange(3, 15)
        self.sg_slider.setValue(5)
        self.sg_label = QLabel("5 pts")
        sg_layout.addWidget(self.sg_slider)
        sg_layout.addWidget(self.sg_label)
        plot_layout.addLayout(sg_layout)

        self.sg_poly_checkbox = QCheckBox("quadratic")
        plot_layout.addWidget(self.sg_poly_checkbox)

        main_layout.addLayout(plot_layout)

        # Buttons for save/cancel
        button_layout = QHBoxLayout()
        self.save_button = QPushButton("Save")
        self.cancel_button = QPushButton("Cancel")
        button_layout.addWidget(self.save_button)
        button_layout.addWidget(self.cancel_button)

        main_layout.addLayout(button_layout)

        # Set main layout
        self.setLayout(main_layout)

        # Connect Signals to update labels dynamically
        self.exposure_slider.valueChanged.connect(self.update_exposure_label)
        self.gain_slider.valueChanged.connect(self.update_gain_label)
        self.roi_slider.valueChanged.connect(self.update_roi_label)
        self.avg_slider.valueChanged.connect(self.update_avg_label)
        self.boxcar_slider.valueChanged.connect(self.update_boxcar_label)
        self.raman_slider.valueChanged.connect(self.update_raman_label)
        self.sg_slider.valueChanged.connect(self.update_sg_label)

        self.file_browse_button.clicked.connect(self.browse_file)

    def update_exposure_label(self, value):
        self.exposure_label.setText(f"{value} ms")

    def update_gain_label(self, value):
        self.gain_label.setText(f"{value / 10.0} dB")

    def update_roi_label(self, value):
        self.roi_label.setText(f"{value} px")

    def update_avg_label(self, value):
        self.avg_label.setText(f"{value}")

    def update_boxcar_label(self, value):
        self.boxcar_label.setText(f"{value}")

    def update_raman_label(self, value):
        self.raman_label.setText(f"{value} nm")

    def update_sg_label(self, value):
        self.sg_label.setText(f"{value} pts")

    def browse_file(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "Save File", "", "CSV files (*.csv);;All Files (*)")
        if file_name:
            self.file_line_edit.setText(file_name)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = CustomDialog()
    dialog.show()
    sys.exit(app.exec())

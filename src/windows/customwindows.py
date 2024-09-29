from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QSpinBox, QDialogButtonBox, QSlider, QProgressBar, QHBoxLayout, \
    QComboBox, QCheckBox
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

        # Checkboxes for plot settings
        self.blank_removal_checkbox = QCheckBox("Enable Blank Removal")
        self.baseline_removal_checkbox = QCheckBox("Enable Baseline Removal (Schulze et al.)")
        self.sgolay_checkbox = QCheckBox("Enable Savitzky-Golay Filtering (post process)")
        plot_layout.addWidget(self.blank_removal_checkbox)
        plot_layout.addWidget(self.baseline_removal_checkbox)
        plot_layout.addWidget(self.sgolay_checkbox)

        # Savitzky-Golay settings
        sg_layout = QVBoxLayout()
        sg_layout.addWidget(QLabel("Window size:"))
        self.sg_slider_window = QSlider(Qt.Horizontal)
        self.sg_slider_window.setRange(3, 15)
        self.sg_slider_window.setValue(5)
        self.sg_label_window = QLabel("5 pts")
        sg_layout.addWidget(self.sg_slider_window)
        sg_layout.addWidget(self.sg_label_window)
        plot_layout.addLayout(sg_layout)

        sg_layout.addWidget(QLabel("Ployorder:"))
        self.sg_slider_polyorder = QSlider(Qt.Horizontal)
        self.sg_slider_polyorder.setRange(1, 5)
        self.sg_slider_polyorder.setValue(1)
        self.sg_label_polyorder = QLabel("1")
        sg_layout.addWidget(self.sg_slider_polyorder)
        sg_layout.addWidget(self.sg_label_polyorder)
        plot_layout.addLayout(sg_layout)

        sg_layout.addWidget(QLabel("Derivative:"))
        self.sg_slider_der = QSlider(Qt.Horizontal)
        self.sg_slider_der.setRange(0, 1)
        self.sg_slider_der.setValue(0)
        self.sg_label_der = QLabel("0")
        sg_layout.addWidget(self.sg_slider_der)
        sg_layout.addWidget(self.sg_label_der)
        plot_layout.addLayout(sg_layout)

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
        layout.addLayout(plot_layout)
        layout.addWidget(self.button_box)

        # Set layout to the dialog
        self.setLayout(layout)

        # Connect Signals to update labels dynamically
        self.boxcar_slider.valueChanged.connect(self.update_boxcar_label)
        self.sg_slider_window.valueChanged.connect(self.update_slider_window_label)
        self.sg_slider_polyorder.valueChanged.connect(self.update_slider_polyorder_label)
        self.sg_slider_der.valueChanged.connect(self.update_slider_der_label)

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

    def update_boxcar_label(self, value):
        self.boxcar_label.setText(f"{value}")
    
    def update_slider_window_label(self, value):
        self.sg_label_window.setText(f"{value} pts")
    
    def update_slider_polyorder_label(self, value):
        self.sg_label_polyorder.setText(value)

    def update_slider_der_label(self, value):
        self.sg_label_der.setText(value)

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
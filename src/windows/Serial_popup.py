from PySide6.QtWidgets import QDialog, QDialogButtonBox, QFormLayout, QLabel, QComboBox
from PySide6 import QtSerialPort
from pyflycap2.interface import Camera, CameraContext


class Serial_popup(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Serial Connection")

        self.serial_comboBox = QComboBox()
        cc = CameraContext()
        for info in cc.get_gige_cams():
            print(info)
            self.serial_comboBox.addItem(str(info))
            
        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        message = QLabel("Select Serial Camera")
        self.layout = QFormLayout()
        self.layout.addWidget(message)
        self.layout.addRow("Serial number: ", self.serial_comboBox)
        self.layout.addWidget(self.buttonBox)
        self.setFixedSize(300,120)

        
        self.setLayout(self.layout)

    def get_results(self):
        return self.serial_comboBox.currentText()
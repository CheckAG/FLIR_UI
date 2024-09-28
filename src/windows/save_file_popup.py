from PySide6.QtWidgets import QDialog, QDialogButtonBox, QFormLayout, QLabel, QComboBox

Supported_filetypes = ['csv']

class Save_file_popup(QDialog):
    def __init__(self):
        super().__init__()

        self.filetype_comboBox = QComboBox()
        self.filetype_comboBox.addItems(Supported_filetypes)


        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        message = QLabel("Select File Parameters")
        self.layout = QFormLayout()
        self.layout.addWidget(message)
        self.layout.addRow("File Type: ", self.filetype_comboBox)
        self.layout.addWidget(self.buttonBox)
        self.setFixedSize(300,300)

        self.setLayout(self.layout)

    def get_options(self) -> str:
        return self.filetype_comboBox.currentText()
from PyQt5 import QtWidgets
from generated.about_temp import Ui_Dialog


class About(Ui_Dialog, QtWidgets.QDialog):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setupUi(self)
        self.setModal(False)
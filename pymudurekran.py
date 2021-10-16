from PyQt5.QtWidgets import *
from mudurekran import Ui_mudurekran

class Mudurekran (QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_mudurekran()
        self.ui.setupUi(self)



from PyQt5.QtWidgets import *          #temel widgetları çağırır
from PyQt5.QtGui import QIcon
from mainPage import Ui_MainWindow
from pymudurekran import Mudurekran


class anaekran(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon("icons/fabrika.png"))    #program icon
        self.ui.line_pass.setEchoMode(QLineEdit.Password)  #şifreli gösterme
        self.ui.line_id.setMaxLength(20)                    #harf uzunluk kısıtlama
        self.ui.line_pass.setMaxLength(20)
        self.ui.pushButton_enter.clicked.connect(self.login)



    def login(self):
        id = self.ui.line_id.text()
        pw = self.ui.line_pass.text()



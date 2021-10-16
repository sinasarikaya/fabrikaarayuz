# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/buraq/PycharmProjects/proje/qt_designer.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QPushButton


class Ui_MainWindow(object):
    pushButton_enter = ...  # type: QPushButton

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(914, 690)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setStyleSheet("#centralwidget {\n"
"border-image: url(:/icons/icons/—Pngtree—modern industrial factory_5418694.png);\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(440, 10, 341, 311))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 20)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.formFrame = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.formFrame.setStyleSheet("#formFrame{\n"
"background-color: rgb(111, 111, 111);\n"
"border-radius : 5px\n"
"}")
        self.formFrame.setObjectName("formFrame")
        self.formLayout = QtWidgets.QFormLayout(self.formFrame)
        self.formLayout.setObjectName("formLayout")
        self.label_id = QtWidgets.QLabel(self.formFrame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_id.setFont(font)
        self.label_id.setStyleSheet("color: rgb(238, 119, 15);")
        self.label_id.setObjectName("label_id")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_id)
        self.line_pass = QtWidgets.QLineEdit(self.formFrame)
        self.line_pass.setMinimumSize(QtCore.QSize(0, 30))
        self.line_pass.setAlignment(QtCore.Qt.AlignCenter)
        self.line_pass.setObjectName("line_pass")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.line_pass)
        self.line_id = QtWidgets.QLineEdit(self.formFrame)
        self.line_id.setMinimumSize(QtCore.QSize(0, 30))
        self.line_id.setText("")
        self.line_id.setAlignment(QtCore.Qt.AlignCenter)
        self.line_id.setObjectName("line_id")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.line_id)
        self.label_pass = QtWidgets.QLabel(self.formFrame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_pass.setFont(font)
        self.label_pass.setStyleSheet("color: rgb(238, 119, 15);")
        self.label_pass.setObjectName("label_pass")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_pass)
        self.horizontalLayout_2.addWidget(self.formFrame)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.pushButton_enter = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_enter.sizePolicy().hasHeightForWidth())
        self.pushButton_enter.setSizePolicy(sizePolicy)
        self.pushButton_enter.setMinimumSize(QtCore.QSize(50, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_enter.setFont(font)
        self.pushButton_enter.setStyleSheet("background-color: rgb(111, 111, 111);\n"
"color: rgb(238, 119, 15);\n"
"border -radius : 5px")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/login.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_enter.setIcon(icon)
        self.pushButton_enter.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_enter.setObjectName("pushButton_enter")
        self.horizontalLayout.addWidget(self.pushButton_enter)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FABRİKA GİRİŞ ANA EKRANI"))
        self.label_id.setText(_translate("MainWindow", "Kullanıcı Adı ="))
        self.label_pass.setText(_translate("MainWindow", "Şifre = "))
        self.pushButton_enter.setText(_translate("MainWindow", "Giriş"))

import icons_rc

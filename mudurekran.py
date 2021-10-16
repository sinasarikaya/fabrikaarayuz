# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/buraq/PycharmProjects/proje/mudurekran.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mudurekran(object):
    def setupUi(self, mudurekran):
        mudurekran.setObjectName("mudurekran")
        mudurekran.resize(754, 622)
        mudurekran.setMinimumSize(QtCore.QSize(600, 400))
        mudurekran.setMaximumSize(QtCore.QSize(754, 622))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/admin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mudurekran.setWindowIcon(icon)
        mudurekran.setStyleSheet("#mudurekran\n"
"{\n"
"border-image: url(:/icons/icons/—Pngtree—modern industrial factory_5418694.png);\n"
"}")
        self.horizontalLayoutWidget = QtWidgets.QWidget(mudurekran)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(280, 20, 351, 281))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.pushButton_kullaniciislem = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_kullaniciislem.sizePolicy().hasHeightForWidth())
        self.pushButton_kullaniciislem.setSizePolicy(sizePolicy)
        self.pushButton_kullaniciislem.setMinimumSize(QtCore.QSize(50, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_kullaniciislem.setFont(font)
        self.pushButton_kullaniciislem.setStyleSheet("background-color: rgb(111, 111, 111);\n"
"color: rgb(238, 119, 15);\n"
"border -radius : 5px")
        self.pushButton_kullaniciislem.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_kullaniciislem.setObjectName("pushButton_kullaniciislem")
        self.verticalLayout.addWidget(self.pushButton_kullaniciislem)
        spacerItem2 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.pushButton_makinaislem = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_makinaislem.sizePolicy().hasHeightForWidth())
        self.pushButton_makinaislem.setSizePolicy(sizePolicy)
        self.pushButton_makinaislem.setMinimumSize(QtCore.QSize(50, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_makinaislem.setFont(font)
        self.pushButton_makinaislem.setStyleSheet("background-color: rgb(111, 111, 111);\n"
"color: rgb(238, 119, 15);\n"
"border -radius : 5px")
        self.pushButton_makinaislem.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_makinaislem.setObjectName("pushButton_makinaislem")
        self.verticalLayout.addWidget(self.pushButton_makinaislem)
        spacerItem3 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.pushButton_anaekrandon = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_anaekrandon.sizePolicy().hasHeightForWidth())
        self.pushButton_anaekrandon.setSizePolicy(sizePolicy)
        self.pushButton_anaekrandon.setMinimumSize(QtCore.QSize(50, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_anaekrandon.setFont(font)
        self.pushButton_anaekrandon.setStyleSheet("background-color: rgb(111, 111, 111);\n"
"color: rgb(238, 119, 15);\n"
"border -radius : 5px")
        self.pushButton_anaekrandon.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_anaekrandon.setObjectName("pushButton_anaekrandon")
        self.verticalLayout.addWidget(self.pushButton_anaekrandon)
        spacerItem4 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)

        self.retranslateUi(mudurekran)
        QtCore.QMetaObject.connectSlotsByName(mudurekran)

    def retranslateUi(self, mudurekran):
        _translate = QtCore.QCoreApplication.translate
        mudurekran.setWindowTitle(_translate("mudurekran", "Müdür Ana Ekranı"))
        self.pushButton_kullaniciislem.setText(_translate("mudurekran", "Kullanıcı İşlemleri"))
        self.pushButton_makinaislem.setText(_translate("mudurekran", "Makina İşlemleri"))
        self.pushButton_anaekrandon.setText(_translate("mudurekran", "Ana Ekrana Dön"))

import icons_rc

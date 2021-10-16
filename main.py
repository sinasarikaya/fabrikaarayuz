from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from calisanekran import Ui_calisanekran
from mudurekran import Ui_mudurekran
from mainPage import Ui_MainWindow
from mudurkayit import Ui_mudurkayit
from mudurmakina import Ui_mudurmakina
from calisanmakina import Ui_calisanmakina
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import sqlite3
import sys
import numpy as np
import matplotlib.pyplot as pt


class mudurKayit(QWidget):
    def __init__(self):
        super().__init__()
        self.mudurKayitUI=Ui_mudurkayit()
        self.mudurKayitUI.setupUi(self)
        self.mudurKayitUI.btn_geridon.clicked.connect(self.goBack)
        self.mudurKayitUI.btn_sil.clicked.connect(self.deletePerson)
        self.mudurKayitUI.btn_ara.clicked.connect(self.searchPerson)
        self.mudurKayitUI.btn_ekle.clicked.connect(self.addPerson)
        self.mudurKayitUI.btn_guncel.clicked.connect(self.update)
        self.update()

    def goBack(self):
        self.close()
    def deletePerson(self):
        user = self.mudurKayitUI.tbWidget_bilgiler.selectedIndexes()
        for i in user:

            mycursor.execute("delete from calisan where tcno like '" + self.mudurKayitUI.tbWidget_bilgiler.item((i.row()),4).text() + "'")
            connection.commit()
        self.update()
    def searchPerson(self):
        items = self.mudurKayitUI.tbWidget_bilgiler.findItems(self.mudurKayitUI.lineEdit_kulaniciad.text(),Qt.MatchExactly)
        if items:
            item = items[0]
            if item == "":
                return
            self.mudurKayitUI.tbWidget_bilgiler.setCurrentItem(item)
            self.mudurKayitUI.tbWidget_bilgiler.scrollToItem(item)
        # for i in item:
        #     i.setSelected(True)
        #     self.mudurKayitUI.tbWidget_bilgiler.scrollToItem(i)
        control = self.mudurKayitUI.tbWidget_bilgiler.selectedItems()
        if control == []:
            m = QtWidgets.QMessageBox()
            m.setWindowTitle('Uyarı!!')
            m.setText('Aradığınız Makina Kayıtlı Değil!!!')
            m.exec_()
    def addPerson(self):
        mycursor.execute("select kullaniciadi from calisan where kullaniciadi like '"+self.mudurKayitUI.lineEdit_kulaniciad.text()+"'")
        UserNames =mycursor.fetchall()
        mycursor.execute("select tcno from calisan where tcno like '"+self.mudurKayitUI.lineEdit_tc.text()+"'")
        IDs = mycursor.fetchall()
        date = self.mudurKayitUI.cw_dtarihi.selectedDate()
        if len(UserNames)!=0 or len(IDs)!=0:
            msg=QtWidgets.QMessageBox()
            msg.setText("Bu kullanıcı Kayıtlı!!!")
            msg.exec_()
            return

        if self.mudurKayitUI.lineEdit_tc.text()=="" or self.mudurKayitUI.lineEdit_kulaniciad.text()=="" or self.mudurKayitUI.lineEdit_sifre.text()==""or self.mudurKayitUI.lineEdit_ad.text()=="" or self.mudurKayitUI.lineEdit_soyad.text()=="" or self.mudurKayitUI.lineEdit_soyad_2.text()=="" or self.mudurKayitUI.comboBox_cinsiyet.currentText()=="" or date.toString()=="":
            msg=QtWidgets.QMessageBox()
            msg.setText("Bilgiler Boş Bırakılamaz!!")
            msg.exec_()
            return
        query="insert into calisan values('"+self.mudurKayitUI.lineEdit_kulaniciad.text()+\
              "','"+self.mudurKayitUI.lineEdit_sifre.text()+\
              "','"+self.mudurKayitUI.lineEdit_ad.text()+\
              "','"+self.mudurKayitUI.lineEdit_soyad.text()+\
              "',"+self.mudurKayitUI.lineEdit_tc.text()+\
              ",'"+self.mudurKayitUI.lineEdit_soyad_2.text()+\
              "','"+self.mudurKayitUI.comboBox_cinsiyet.currentText()+\
              "','"+date.toString()+\
              "','"+\
              "calisan"+"')"
        mycursor.execute(query)
        connection.commit()
        self.update()
    def update(self):
        mycursor.execute("select * from calisan")
        result = mycursor.fetchall()
        for i in range(49):
            for j in range(9):
                self.mudurKayitUI.tbWidget_bilgiler.setItem(i,j,QtWidgets.QTableWidgetItem(""))
        for i in range(len(result)):
            for j in range(len(result[i])):
                self.mudurKayitUI.tbWidget_bilgiler.setItem(i,j,QtWidgets.QTableWidgetItem((result[i][j])))
class mudurMakina(QWidget):
    def __init__(self):
        super().__init__()
        self.mudurMakinaUI=Ui_mudurmakina()
        self.mudurMakinaUI.setupUi(self)
        self.mudurMakinaUI.btn_mgeridon.clicked.connect(self.goBack)
        self.mudurMakinaUI.btn_mekle.clicked.connect(self.addMachine)
        self.mudurMakinaUI.btn_mguncel.clicked.connect(self.updateMachine)
        self.mudurMakinaUI.btn_msil.clicked.connect(self.deleteMachine)
        self.mudurMakinaUI.btn_mara.clicked.connect(self.searchMachine)
        self.mudurMakinaUI.btn_mgrafik.clicked.connect(self.graph)
        self.updateMachine()


    def graph(self):
        mycursor.execute("select sicaklik from makina")
        degree = mycursor.fetchall()
        mycursor.execute("select basinc from makina")
        bar = mycursor.fetchall()
        valuesdegree = []
        valuesbar = []
        for i in range(len(bar) - 1):
            valuesdegree.append(degree[i][0])
            valuesbar.append(bar[i][0])
        a = range(len(bar) - 1)
        pt.plot(a, valuesdegree, label='sıcaklık')
        pt.plot(a, valuesbar, label='basınç')
        pt.title('Basınç ve Sıcaklık Grafiği')
        pt.legend()
        pt.show()

    def searchMachine(self):
        items = self.mudurMakinaUI.tbWidget_bilgiler.findItems(self.mudurMakinaUI.lineEdit_model.text(),                                                      Qt.MatchExactly)
        if items:
            item = items[0]
            if item == "":
                return
            self.mudurMakinaUI.tbWidget_bilgiler.setCurrentItem(item)
            self.mudurMakinaUI.tbWidget_bilgiler.scrollToItem(item)
        control = self.mudurMakinaUI.tbWidget_bilgiler.selectedItems()
        if control == []:
            m = QtWidgets.QMessageBox()
            m.setWindowTitle('Uyarı!!')
            m.setText('Aradığınız Makina Kayıtlı Değil!!!')
            m.exec_()
    def deleteMachine(self):
        user = self.mudurMakinaUI.tbWidget_bilgiler.selectedIndexes()
        for i in user:

            mycursor.execute(
                "delete from makina where makinamodel like '" + self.mudurMakinaUI.tbWidget_bilgiler.item((i.row()),0).text() + "'")
            connection.commit()
        self.updateMachine()
    def updateMachine(self):
        mycursor.execute("select * from makina")
        result = mycursor.fetchall()
        for i in range(49):
            for j in range(4):
                self.mudurMakinaUI.tbWidget_bilgiler.setItem(i, j, QtWidgets.QTableWidgetItem(""))
        for i in range(len(result)):
            for j in range(len(result[i])):
                self.mudurMakinaUI.tbWidget_bilgiler.setItem(i, j, QtWidgets.QTableWidgetItem(str(result[i][j])))
    def addMachine(self):
        mycursor.execute("select makinamodel from makina where makinamodel like '" + self.mudurMakinaUI.lineEdit_model.text() + "'")
        IDs = mycursor.fetchall()
        if len(IDs) != 0:
            msg = QtWidgets.QMessageBox()
            msg.setText("Bu makina Kayıtlı!!!")
            msg.exec_()
            return
        date = self.mudurMakinaUI.cw_eklenmet.selectedDate()
        if self.mudurMakinaUI.lineEdit_model.text() =="" or self.mudurMakinaUI.lineEdit_basinc.text()=="" or self.mudurMakinaUI.lineEdit_sicaklik.text()=="":
            msg = QtWidgets.QMessageBox()
            msg.setText("Bilgiler Boş Bırakılamaz!!")
            msg.exec_()
            return
        query = "insert into makina values(" \
                "'"+self.mudurMakinaUI.lineEdit_model.text()+"'," \
                "'"+self.mudurMakinaUI.lineEdit_sicaklik.text()+"'," \
                "'"+self.mudurMakinaUI.lineEdit_basinc.text()+"',"\
                "'"+date.toString()+"')"
        mycursor.execute(query)
        connection.commit()
        self.updateMachine()
    def goBack(self):
        self.close()
class Mudurekran (QWidget):

    def __init__(self):
        super().__init__()
        self.mudurEkranUI = Ui_mudurekran()
        self.mudurEkranUI.setupUi(self)
        self.mudurKayitUI=mudurKayit()
        self.mudurMakinaUI=mudurMakina()
        self.mudurEkranUI.pushButton_anaekrandon.clicked.connect(self.goMainPage)
        self.mudurEkranUI.pushButton_kullaniciislem.clicked.connect(self.goEditPerson)
        self.mudurEkranUI.pushButton_makinaislem.clicked.connect(self.goMachine)
    def goMainPage(self):
        window.show()
        self.mudurKayitUI.close()
        self.mudurMakinaUI.close()
        self.close()

    def goEditPerson(self):
        self.mudurKayitUI.show()
        self.mudurMakinaUI.close()
    def goMachine(self):
        self.mudurMakinaUI.show()
        self.mudurKayitUI.close()





class calisanMakina(QWidget):
    def __init__(self):
        super(calisanMakina, self).__init__()
        self.calisanMakinaUI=Ui_calisanmakina()
        self.calisanMakinaUI.setupUi(self)
        self.calisanMakinaUI.btn_kekle.clicked.connect(self.addMachine)
        self.calisanMakinaUI.btn_kgeridon.clicked.connect(self.goBack)
        self.calisanMakinaUI.btn_kguncel.clicked.connect(self.update)
        self.calisanMakinaUI.btn_kara.clicked.connect(self.search)
        self.calisanMakinaUI.btn_kgrafik.clicked.connect(self.graph)
        self.update()
    def graph(self):
        mycursor.execute("select sicaklik from makina")
        degree = mycursor.fetchall()
        mycursor.execute("select basinc from makina")
        bar = mycursor.fetchall()
        valuesdegree = []
        valuesbar = []
        for i in range(len(bar) - 1):
            valuesdegree.append(degree[i][0])
            valuesbar.append(bar[i][0])
        a = range(len(bar) - 1)
        pt.plot(a, valuesdegree, label='sıcaklık')
        pt.plot(a, valuesbar, label='basınç')
        pt.title('Basınç ve Sıcaklık Grafiği')
        pt.legend()
        pt.show()
    def addMachine(self):
        mycursor.execute(
            "select makinamodel from makina where makinamodel like '" + self.calisanMakinaUI.lineEdit_kmodel.text() + "'")
        IDs = mycursor.fetchall()
        if len(IDs) != 0:
            msg = QtWidgets.QMessageBox()
            msg.setText("Bu makina Kayıtlı!!!")
            msg.exec_()
            return
        date = self.calisanMakinaUI.cw_keklenmet.selectedDate()
        if self.calisanMakinaUI.lineEdit_kmodel.text() == "" or self.calisanMakinaUI.lineEdit_kbasinc.text() == "" or self.calisanMakinaUI.lineEdit_ksicaklik.text() == "":
            msg = QtWidgets.QMessageBox()
            msg.setText("Bilgiler Boş Bırakılamaz!!")
            msg.exec_()
            return
        query = "insert into makina values(" \
                "'" + self.calisanMakinaUI.lineEdit_kmodel.text() + "'," \
                "'" + self.calisanMakinaUI.lineEdit_ksicaklik.text() + "'," \
                "'" + self.calisanMakinaUI.lineEdit_kbasinc.text() + "'," \
                "'" + date.toString() + "')"
        mycursor.execute(query)
        connection.commit()
        self.update()
    def goBack(self):
        self.close()
    def update(self):
        mycursor.execute("select * from makina")
        result = mycursor.fetchall()
        for i in range(49):
            for j in range(4):
                self.calisanMakinaUI.tbWidget_kbilgiler.setItem(i, j, QtWidgets.QTableWidgetItem(""))
        for i in range(len(result)):
            for j in range(len(result[i])):
                self.calisanMakinaUI.tbWidget_kbilgiler.setItem(i, j, QtWidgets.QTableWidgetItem(str(result[i][j])))
    def search(self):
        items = self.calisanMakinaUI.tbWidget_kbilgiler.findItems(self.calisanMakinaUI.lineEdit_kmodel.text(),
                                                               Qt.MatchExactly)
        if items:
            item = items[0]
            if item == "":
                return
            self.calisanMakinaUI.tbWidget_kbilgiler.setCurrentItem(item)
            self.calisanMakinaUI.tbWidget_kbilgiler.scrollToItem(item)
        control = self.calisanMakinaUI.tbWidget_kbilgiler.selectedItems()
        if control == []:
            m = QtWidgets.QMessageBox()
            m.setWindowTitle('Uyarı!!')
            m.setText('Aradığınız Makina Kayıtlı Değil!!!')
            m.exec_()

class CalisanEkran (QWidget):

    def __init__(self):
        super().__init__()
        self.calisanUI = Ui_calisanekran()
        self.calisanUI.setupUi(self)
        self.calisanMakinaUI=calisanMakina()

        self.calisanUI.pb_canaekrandon.clicked.connect(self.goBackMain)
        self.calisanUI.pb_cmakinaislem.clicked.connect(self.goMachine)

    def goBackMain(self):
        window.show()
        self.calisanMakinaUI.hide()
        self.close()
    def goMachine(self):
        self.calisanMakinaUI.show()

class anaekran(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon("icons/fabrika.png"))  # program icon
        self.ui.line_pass.setEchoMode(QLineEdit.Password)  # şifreli gösterme
        self.ui.line_id.setMaxLength(20)  # harf uzunluk kısıtlama
        self.ui.line_pass.setMaxLength(20)
        self.ui.pushButton_enter.clicked.connect(self.login)

        # pages
        self.managerPage=Mudurekran()
        self.employeePage=CalisanEkran()

    def login(self):
        id = self.ui.line_id.text()
        pw = self.ui.line_pass.text()
        mycursor.execute("select * from calisan where kullaniciadi like '"+id+"'")
        idCheck=mycursor.fetchall()
        if len(idCheck)==0:
            return
        if id ==idCheck[0][0] and pw == idCheck[0][1]:
            if idCheck[0][8]=="mudur":
                self.managerPage.show()
                window.hide()
            else:
                self.employeePage.show()
                window.hide()








def RunApp():
    global window, connection, mycursor
    connection = sqlite3.connect('calisantablo.db')
    mycursor = connection.cursor()
    app = QtWidgets.QApplication(sys.argv)
    window = anaekran()
    window.show()
    sys.exit(app.exec_())


RunApp()






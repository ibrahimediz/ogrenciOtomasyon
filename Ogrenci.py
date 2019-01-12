from PyQt5 import QtCore, QtGui, uic
import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow,QMessageBox, QApplication, QWidget,QFileDialog,QTableWidgetItem
from OgrenciDB import OgrenciDB
class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.veri = OgrenciDB()
        uic.loadUi(r'D:\İbrahim EDİZ\Projem\ogrenciOtomasyon\Ogrenci.ui', self)
        self.Kaydet.clicked.connect(self.oKaydet)
        self.btGuncelle.clicked.connect(self.oGuncelle)
        self.ogrListeDoldur()
        self.show()
    def oKaydet(self):
        tc = self.txtTC.text()
        adi = self.veri.strGonder(self.txtAdi.text())
        soyadi = self.veri.strGonder(self.txtSoyadi.text())
        cinsiyet = -1
        if self.rdbKiz.isChecked():
            cinsiyet = 0
        if self.rdbErkek.isChecked():
            cinsiyet = 1
        sonuc = self.veri.OgrenciEkle(Degerler=[tc,adi,soyadi,cinsiyet])
        if sonuc == "1":
            QMessageBox.information(self,"Bilgi","Kayıt İşlemi Başarılı",QMessageBox.Ok,QMessageBox.Ok)
        else:
            print(sonuc)
    def oGuncelle(self):
        tc = self.txtTC.text()
        adi = self.veri.strGonder(self.txtAdi.text())
        soyadi = self.veri.strGonder(self.txtSoyadi.text())
        cinsiyet = -1
        if self.rdbKiz.isChecked():
            cinsiyet = 0
        if self.rdbErkek.isChecked():
            cinsiyet = 1
        ID = int(self.lblogrno.text())
        sonuc = self.veri.OgrenciGuncelle(Degerler=[tc,adi,soyadi,cinsiyet],ID=ID)
        if sonuc == "1":
            QMessageBox.information(self,"Bilgi","Güncelleme İşlemi Başarılı",QMessageBox.Ok,QMessageBox.Ok)
            self.ogrListeDoldur()
        else:
            print(sonuc)
    def ogrListeDoldur(self):
        self.OgrListe = self.veri.OgrListeGetir()
        self.ogrListe.doubleClicked.connect(self.kayitSec)
        self.ogrListe.setRowCount(len(self.OgrListe))
        self.ogrListe.setColumnCount(len(self.OgrListe[0]))
        for i in range(0,len(self.OgrListe)):
            for j in range(0,len(self.OgrListe[0])):
                self.ogrListe.setItem(i,j, QTableWidgetItem(str(self.OgrListe[i][j])))


    def kayitSec(self):
        for currentQTableWidgetItem in self.ogrListe.selectedItems():
            adi = str(self.OgrListe[int(currentQTableWidgetItem.row())][2]).split(' ')[0]
            self.txtAdi.setText(adi)
            soyadi=str(self.OgrListe[int(currentQTableWidgetItem.row())][2]).split(' ')[1]
            self.txtSoyadi.setText(soyadi)
            tc=str(self.OgrListe[int(currentQTableWidgetItem.row())][1])
            self.txtTC.setText(tc)
            self.lblogrno.setText(str(self.OgrListe[int(currentQTableWidgetItem.row())][0]))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_()) 
    
from PyQt5 import QtCore, QtGui, uic
import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow,QMessageBox, QApplication, QWidget,QFileDialog
from OgrenciDB import OgrenciDB
class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.veri = OgrenciDB()
        uic.loadUi(r'D:\İbrahim EDİZ\Projem\ogrenciOtomasyon\Ogrenci.ui', self)
        self.Kaydet.clicked.connect(self.oKaydet)
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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_()) 
    
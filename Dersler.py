from PyQt5 import QtCore, QtGui, uic
import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow,QMessageBox, QApplication, QWidget,QFileDialog
from DB import VeriTabani
class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.veri = VeriTabani(r"D:\İbrahim EDİZ\Projem\ogrenciOtomasyon\OgrenciOT.db")
        uic.loadUi(r'D:\İbrahim EDİZ\Projem\ogrenciOtomasyon\Ders2.ui', self)
        self.btKaydet.clicked.connect(self.Kaydet)
        self.show()
    def Kaydet(self):
        sonuc = self.veri.insert(Tablo="DERSLER",
        SUTUN=["DERS_ADI","GRUP"],
        DEger=["'"+self.txtDersAdi.text()+"'",self.txtGrup.text()])
        print(sonuc)
        if sonuc == "1":
            QMessageBox.information(self,"Bilgi","Kayıt İşlemi Başarılı",QMessageBox.Ok,QMessageBox.Ok)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_()) 
    
    
    
    python -m pip install --upgrade pip
    
    pip install PyQt5Designer
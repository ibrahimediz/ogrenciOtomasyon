from DB import VeriTabani
class SinifDB(VeriTabani):
    def __init__(self):
        self.adres = r"D:\İbrahim EDİZ\Projem\ogrenciOtomasyon\OgrenciOT.db"
        super().__init__(self.adres)
        self.TabloAdi = "SINIFLAR"
        self.Sutun = ["SINIF_ADI","SEVIYE"]
    def SinifEkle(self,Degerler = []):
        sonuc = self.insert(Tablo=self.TabloAdi,Sutun=self.Sutun,Deger=Degerler)
        return sonuc
    def SinifGuncelle(self,Degerler=[],ID=0):
        sonuc = self.UpdateWithID(Tablo=self.TabloAdi,Sutun=self.Sutun,Deger=Degerler,ID=ID)
        return sonuc
    def SinifSil(self,ID=0):
        sonuc = self.DeleteWithID(Tablo=self.TabloAdi,ID=ID)
        return sonuc
    def SinifListeGetir(self):
        sonuc = self.select(Tablo="V_SINIF_LISTE")
        return sonuc
     
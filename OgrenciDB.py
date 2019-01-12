from DB import VeriTabani
class OgrenciDB(VeriTabani):
    def __init__(self):
        self.adres = r"D:\İbrahim EDİZ\Projem\ogrenciOtomasyon\OgrenciOT.db"
        super().__init__(self.adres)
        self.TabloAdi = "OGRENCILER"
        self.Sutun = ["OGR_TC","OGR_ADI","OGR_SOYADI","CINSIYET"]
    def OgrenciEkle(self,Degerler = []):
        sonuc = self.insert(Tablo=self.TabloAdi,Sutun=self.Sutun,Deger=Degerler)
        return sonuc
    def OgrenciGuncelle(self,Degerler=[],ID=0):
        sonuc = self.UpdateWithID(Tablo=self.TabloAdi,Sutun=self.Sutun,Deger=Degerler,ID=ID)
        return sonuc
    def OgrListeGetir(self):
        sonuc = self.select(Tablo="V_OGRENCI_LISTE")
        return sonuc
     
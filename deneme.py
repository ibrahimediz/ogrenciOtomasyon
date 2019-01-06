from DB import VeriTabani as vt
veri = vt(r"D:\İbrahim EDİZ\Projem\ogrenciOtomasyon\OgrenciOT.db")
print(veri.insert(Tablo="DERSLER",
Sutun=["DERS_ADI","GRUP"],
Deger=["'Tarih'",0]))


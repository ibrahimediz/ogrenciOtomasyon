from DB import VeriTabani as vt
veri = vt(r"D:\İbrahim EDİZ\Projem\ogrenciOtomasyon\OgrenciOT.db")
print(veri.select(Tablo="Dersler"))
print(veri.select(Tablo="OGRENCILER"))


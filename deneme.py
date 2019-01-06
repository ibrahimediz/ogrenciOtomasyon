from DB import VeriTabani as vt
veri = vt(r"D:\İbrahim EDİZ\Projem\ogrenciOtomasyon\OgrenciOT.db")
# print(veri.DELETEWithID(Tablo="DERSLER",
# Sutun=["DERS_ADI","GRUP"],
# Deger=["'Seçmeli Coğrafya'",1],ID=7))

print(veri.DeleteWithID(Tablo="DERSLER",ID=7))

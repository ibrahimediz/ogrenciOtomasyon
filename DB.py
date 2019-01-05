class VeriTabani():
    def __init__(self,adres):
        self.adres = adres
    
    def select(self,**kwargs):
        import sqlite3
        try:
            adim = "1"
            liste = []
            baglanti = sqlite3.connect(self.adres)
            adim = "1A"
            cur = baglanti.cursor()
            sorgu = "SELECT * FROM "
            for key,value in kwargs.items():
                if key=="Tablo":
                    sorgu += value
            adim = "2A"
            cur.execute(sorgu)
            liste = cur.fetchall()
            adim = "3A"
        except:
            liste.index(0,"Hata :"+adim)
        finally:
            baglanti.close()
            return liste




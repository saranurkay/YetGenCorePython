
#1.soru

def urun_bilgisi(adı, fiyatı):
    with open("urunler.txt","a",encoding="utf-8") as file:
        file.write(f"adı: {adı} fiyatı: {fiyatı}\n")

urun_bilgisi("eski kelime", 15)


#2.soru

def bul_ve_degistir(dosya_ismi,eski_kelime,yeni_kelime):
    with open(dosya_ismi,"r+") as file:
        text = file.read()
        sonhali_text = text.replace(eski_kelime,yeni_kelime)
        file.seek(0)
        file.write(sonhali_text)
        file.truncate()

bul_ve_degistir("urunler.txt","eski kelime","yeni kelime")


#3.soru

class Vehicle:
    def __init__(self, name, speed, mileage):
        self.name = name
        self.speed = speed
        self.mileage = mileage

    def info(self):
        print(f"Name: {self.name} Speed: {self.speed} Mileage: {self.mileage}")

class Bus(Vehicle):
    pass

bus = Bus("School Volvo", 180, 12)
bus.info()


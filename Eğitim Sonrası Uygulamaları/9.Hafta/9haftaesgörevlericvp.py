import random
import time

class Kumanda:
    def __init__(self, tvDurum = "Kapalı", tvSes = 0, kanalListesi = ["Kanal1"], kanal = "Kanal1"):
        self.tvDurum = tvDurum
        self.tvSes = tvSes
        self.kanalListesi = kanalListesi
        self.kanal = kanal
    
    def tvAc(self):
        if (self.tvDurum == "Açık"):
            print("Televizyon açık...")
        else:
            print("Televizyon açılıyor...")
            self.tvDurum = "Açık"
        
    def tvKapat(self):
        if (self.tvDurum == "Kapalı"):
            print("Televizyon zaten kapalı...")
        else:
            print("Televizyon kapanıyor...")
            self.tvDurum = "Kapalı"
    
    def sesAyarları(self):
        while True:
            cevap = input("Sesi azalt: '<'\nSesi arttır: '>'\nÇıkış: çıkış")
            if (cevap == "<"):
                if (self.tvSes != 0):
                    self.tvSes -= 1
                    print("Ses:", self.tvSes)
            elif(cevap == ">"):
                if (self.tvSes != 25):
                    self.tvSes += 1
                    print("Ses:", self.tvSes)
            else:
                print("Ses güncellendi:",self.tvSes)
                break
    def kanalEkle(self, kanalİsmi):
        print("Kanal ekleniyor...")
        time.sleep(1)

        self.kanalListesi.append(kanalİsmi)
        print("Kanal eklendi...")
    
    def rastgeleKanal(self):
        rastgele = random.randint(0, len(self.kanalListesi)-1)
        self.kanal = self.kanalListesi[rastgele]
        print("Şu anki kanal:", self.kanal)
    
    def __len__(self):
        return len(self.kanalListesi)
    def __str__(self):
        return "Tv Durumu: {}\nTv Ses: {}\nKanal Listesi: {}\nŞu anki kanal: {}\n".format(self.tvDurum,self.tvSes,self.kanalSistesi, self.kanal)
    
kumanda = Kumanda(tvSes=0)

print("""
Televizyon Uygulaması
1. Tv Aç
2. Tv Kapat
3. Ses Ayarları
4. Kanal Ekle
5. Kanal Sayısını Öğrenme
6. Rastgele Kanala Geçme
7. Televizyon Bilgileri
Çıkmak için 'q' ya basın.
""")

while True:
    islem = input("İşlemi seçiniz:")
    if (islem == "q"):
        print("Program sonlandırılıyor...")
        break
    elif (islem == "1"):
        kumanda.tvAc()
    elif (islem == "2"):
        kumanda.tvKapat()
    elif (islem == "3"):
        kumanda.sesAyarları()
    elif (islem == "4"):
        kanalİslemleri = input("Kanal işlemlerini ',' ile ayırarak giriniz:")
        kanalListesi =kanalİslemleri.split(",")
        for i in kanalListesi:
            kumanda.kanalEkle(1)
    elif (islem == "5"):
        print("Kanal sayısı:", len(kumanda))
    elif(islem == 6):
        kumanda.rastgeleKanal()
    elif (islem == 7):
        print(kumanda)
    else:
        print("Geçersiz işlem...")

#1.soru

def vki_hesapla(kilo, boy):
    return kilo / ((boy/100) ** 2)

def siniflandir(vki):
    if vki < 18.5:
        return "Zayif"
    elif 18.5 <= vki <= 24.9:
        return "Normal Kilolu"
    elif 25 <= vki <= 29.9:
        return "Fazla Kilolu"
    elif 30 <= vki <= 39.9:
        return "Obez"
    else:
        return "Morbid Obez"

def kaydet(isim, soyisim, yas, boy, kilo):
    vki = vki_hesapla(kilo, boy)
    sinif = siniflandir(vki)
    dosya = open("vki_verileri.txt", "a")
    dosya.write(f"{isim} {soyisim}, {yas} yasida, {boy} cm boyunda, {kilo} kg agirliginda.\n VKI: {vki:.2f}\n Sinif: {sinif}\n")
    dosya.close()

giris_sayisi = int(input("Kac giris yapacaksiniz? "))
for i in range(giris_sayisi):
    isim = input("İsim: ")
    soyisim = input("Soyisim: ")
    yas = int(input("Yas: "))
    boy = int(input("Boy(cm): "))
    kilo = int(input("Kilo(kg): "))
    kaydet(isim, soyisim, yas, boy, kilo)


#2.soru

from datetime import datetime


malzemeler = {
    "Muz": 7,
    "Elma": 4,
    "Çilek": 6,
    "Avokado": 8,
    "Karpuz": 5,
    "Mandalina": 3,
    "Portakal": 5,
    "Kavun": 5,
    "Armut": 4,
    "Ekstasut": 3}


def menu_goruntule():
    print("Malzemeler:")
    for malzeme, fiyat in malzemeler.items():
        print(f"{malzeme}: {fiyat} TL")
    print("")


def fiyat_hesapla(malzeme_listesi):
    toplam_fiyat = 0
    for malzeme in malzeme_listesi:
        if malzeme in malzemeler:
            toplam_fiyat += malzemeler[malzeme]
    return toplam_fiyat


def satin_al(malzeme_listesi):
    fiyat = fiyat_hesapla(malzeme_listesi)
    tarih = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    with open("YetBar.txt", "a") as file:
        file.write(f"{tarih} - {malzeme_listesi} - {fiyat} TL\n")
    print(f"\n{malzeme_listesi} smoothie için ödemeniz gereken tutar: {fiyat} TL.\nAfiyet olsun!\n")

while True:
    print("YetBar'a Smoothie Otomatına Hoşgeldiniz!")
    print("Yapmak istediğiniz işlemi seçin:")
    print("1 - Menüyü görüntüle")
    print("2 - Smoothie içeriği seç ve satın al")
    print("3 - Çıkış yap")
    secim = input("Seçiminiz (1-3): ")

    if secim == "1":
        menu_goruntule()
    elif secim == "2":
        malzemeler_str = input("Lütfen smoothienizin içine eklemek istediğiniz malzemeleri boşluk bırakarak yazın: ")
        malzeme_listesi = [malzeme.strip() for malzeme in malzemeler_str.split(" ")]
        satin_al(malzeme_listesi)
    else:
        print("Lütfen tekrar deneyin.\n")

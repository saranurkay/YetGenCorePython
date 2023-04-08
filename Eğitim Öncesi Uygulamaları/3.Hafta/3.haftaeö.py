
#1.soru


sayi = int(input("Bir sayı giriniz: "))

if sayi % 7 == 0:
    print("Sayı 7'ye tam bölünüyor")
else:
    print("Sayı 7'ye tam bölünmüyor")
    

#2. soru


vize = float(input("Vize notunuzu gir:"))
final = float(input("Final notunuzu gir:"))
ortalama = (vize*0.4) + (final*0.6)
print("Ortalama: " + str(ortalama))
if final >= 50:
    if ortalama >= 85:
        print("AA alarak geçtiniz.")
    elif ortalama >= 75:
        print("BA alarak  geçtiniz.")
    elif ortalama >= 70:
        print("BB alarak  geçtiniz.")
    elif ortalama >= 65:
        print("CB alarak  geçtiniz.")
    elif ortalama >= 60:
        print("CC alarak  geçtiniz.")
    elif ortalama >= 55:
        print("DC alarak  geçtiniz.")
    elif ortalama >= 50:
        print("DD alarak  geçtiniz.")
    else:
        print("FF alarak kaldınız.")
        
else:
    print("FF alarak kaldınız.")
    
    
#3.soru

yas1 = int(input("1.yas giriniz:"))
yas2 = int(input("2.yas giriniz:"))

if yas1 > yas2:
    print("1.yas Büyüktür. yas:" + str(yas1))
if yas2 > yas1:
    print("2.yas Büyüktür. yas:" + str(yas2))
else:
    print("İki yas Birbirine Eşittir.")
    
    
#4.soru

ates = float(input("Ateşini gir:"))
if ates >= 37.5:
    print("Ateşi " + str(ates) + " derece. AVM'ye girebilirsin! Maske takmayı unutma!")
else:
    print("Ateş " + str(ates) + " derece. AVM'ye giremezsin! Hemen evine dön!")


#5.soru

boy = float(input("Boyunuzu Giriniz:"))
kilo = float(input("Kilonuzu Giriniz:"))
bki = kilo/(boy**2)

if bki< 18.5:
    print("Zayıfsınız")
elif bki < 25:
    print("Normal Kilo")
elif bki < 30:
    print("Fazla Kilolusunuz")
else:
    print("Obezsiniz")
    
#6.soru

isim = input("İsminizi Giriniz:")
yas = int(input("Yaşınızı Giriniz:"))
egitim = input("Eğitim Durumunuzu Giriniz:")
 
if yas >=18:
    if (egitim == 'Lise' or egitim =='Üniversite' or egitim == 'üniversite' or egitim == "lise"):
        print(f"{isim} ehliyet alabilirsiniz.")
    else:
        print(f"{isim} ehliyet alma şartını yaşınız karşılasa da eğitim durumunuz karşılamıyor.")

else:
    print("Her iki koşulu da sağlamadığınız için ehliyet alamazsınız.")
    

#7.soru

yil=int(input("Yıl giriniz:"))

if yil%4==0 and yil % 100 !=0:
    print(f"{yil} artık yıldır.")
elif yil%400==0:
    print(f"{yil} artık yıldır.")
else:
    print(f"{yil} artık yıl değildir.")

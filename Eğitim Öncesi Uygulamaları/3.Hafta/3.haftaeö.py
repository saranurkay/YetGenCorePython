# -*- coding: utf-8 -*-
"""
@author: sara
"""

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
print("yapamadım")
#6.soru
print("yapamadım")
#7.soru
print("eğitimden sonra bak sara")

#!/usr/bin/env python
# coding: utf-8

# # Problem 1 Aradaki Tam Sayılar
# 
# Kullanıcıdan iki adet sayı alınız, bu sayılar arasındaki tam sayıları ekrana yazdıran bir program yazınız. 

# In[ ]:


baslangıc = int(input("İlk sayı: "))
bitis = int(input("İkinci sayı: "))

print("Sayılar arasındaki tam sayılar: ")
for i in range(baslangıc, bitis+1):
    print(i)


# # Problem 2 Faktöriyel
# 
# Kullanıcıdan bir sayı alınız ve alınan sayının faktöriyelini hesaplayan bir program yazınız. 
# 

# In[ ]:


num = int(input("Bir sayı girin: "))

faktoriyel = 1

if num < 0:
    print("Negatif sayıların faktöriyeli hesaplanamaz.")
elif num == 0:
    print("0'ın faktöriyeli = 1")
else:
    for i in range(1, num+1):
        faktoriyel *= i
    print("{}'ın faktöriyeli = {}".format(num, faktoriyel))


# # Problem 3 Virgül ile Ayırma
# 
# Kullanıcıdan bir metin halinde virgül ile ayrılmış sayılar alınız ve aldığınız her bir sayıyı listeye atayınız, daha sonra listedeki her elemanı toplayıp ekrana bastıran bir program yazınız.
# 
# <h4>Sample Input</h4>
# <p>
# Lutfen sayilari virgul ile ayrirarak giriniz: 5,14,7,2,1
# </p>
# <h4>Output</h4>
# 
# Toplam: 29

# In[ ]:


sayi = input("Virgül ile ayırarak sayıları gir: ")
sayi_list = sayi.split(",")

total = 0
for sayi in sayi_list:
    total += int(sayi)

print("Sayıların toplamı: ", total)


# # Problem 4 Büyük Sayı
# 
# Kullanıcıdan alınan iki sayıdan büyük olanı bulup, ekrana yazdıran bir fonksiyon yazınız.

# In[ ]:


def buyuk_sayi_bul(a, b):
    if a > b:
        print("{} büyüktür.".format(a))
    elif b > a:
        print("{} büyüktür.".format(b))
    else:
        print("Girdiğiniz sayılar birbirine eşit.")
sayi1 = float(input("İlk sayıyı gir: "))
sayi2 = float(input("İkinci sayıyı gir: "))
buyuk_sayi_bul(sayi1,sayi2)


# # Problem 5 Ürün Kayıt Uygulaması
# Programımız ilk olarak kullanıcıdan, kaydı yapılacak ürünlerin sayısını isteyecek. Ardından yazılmış olan ürün sayısı kadar ürün ismi ve ürün fiyatı bilgisini kullanıcıdan alacak. Son olarak ise ürünleri ekrana yazdıracağız.
# 
# <h4>Sample Input:</h4>
# <p>
# Lutfen kac adet urun gireceginizi yaziniz: 3
# <br/>
# 1. Urununuzun ismini giriniz: Mentos
# <br/>
# 1. Urununuzun fiyatini giriniz: 1
# <br/>
# 2. Urununuzun ismini giriniz: Meybuz
# <br/>
# 2. Urununuzun fiyatini giriniz: 0.25
# <br/>
# 3. Urununuzun ismini giriniz: Uzun Şeker
# <br/>
# 3. Urununuzun fiyatini giriniz: 0.75
# <br/>
# <h4>Output:</h4>
# 1. Urun: Mentos - 1 TL
# <br/>
# 2. Urun: Meybuz - 0.25 TL
# <br/>
# 3. Urun: Uzun Şeker - 0.75 TL
# </p>

# In[ ]:


urun_sayi = int(input("Kaç adet ürün gireceğinizi yazın: "))

urunler = []

for i in range(urun_sayi):
    urun_isim = input(f"{i+1}. Ürünün ismini yazın: ")
    urun_fiyat = float(input(f"{i+1}. Ürünün fiyatını yazın: "))
    urunler.append({"isim": urun_isim, "fiyat": urun_fiyat})

for i, urun in enumerate(urunler):
    print(f"{i+1}. Ürün: {urun['isim']} - {urun['fiyat']} TL")


# # Problem 6 Türkçe Karakter Çevirici
# Programa girilen dosya ismindeki Türkçe karakterleri, İngilizce'ye çeviren programı yazınız.
# 
# <h4>Sample Input:</h4>
# <p>
# Lutfen dosya ismi giriniz: fotoğraf.jpeg
# <br>
# Dosya ismi: fotograf.jpeg
# <br>
# <br>
# Lutfen dosya ismi giriniz: ışık.png
# <br>
# Dosya ismi: isik.png
# </p>

# In[ ]:


turkce_to_ingilizce = {
    'ı': 'i',
    'İ': 'I',
    'ç': 'c',
    'Ç': 'C',
    'ş': 's',
    'Ş': 'S',
    'ğ': 'g',
    'Ğ': 'G',
    'ü': 'u',
    'Ü': 'U',
    'ö': 'o',
    'Ö': 'O'
}

dosya_adi = input("Lutfen dosya ismi giriniz: ")

for turkce, ingilizce in turkce_to_ingilizce.items():
    dosya_adi = dosya_adi.replace(turkce, ingilizce)

print("Dosya ismi:", dosya_adi)

# # Problem 7 Sayı Tahmin Oyunu ama Bilgisayar Tahmin Ediyor :)
# Sayı tahmin oyunu: İki oyuncudan birinin, 0 ile 100 arasında bir sayı tutması ile başlar. Diğer oyuncu ise tahminler yaparak tutulan sayıyı bulmaya çalışır ve yaptığı her tahminde sayıyı tutmuş olan oyuncudan YUKARI veya AŞAĞI olarak geri bildirim alır. Sayıyı bildiğinde ise rakip oyuncu kaç tahminde (kaç denemede) bildiğini söyler.
# 
# Senden yazmanı beklediğimiz program ise Python'ın tahminleri yapan tarafta olacağı bir oyun oluşturman. Yani sen 0 ile 100 arasında bir sayı tutacaksın ardından program senin tuttuğunuz sayıyı bulmaya çalışacak.
# <h4>Sample Input:</h4>
# Bu örnekte aklınızdan 90 tuttuğunuzu varsayalım.
# <p>
# Oyun başlıyor lutfen aklindan bir sayi tut! Tuttun mu, hazır mısın? : 1
# <br>
# Tahmin: 50
# <br>
# Durum: Yukari
# <br>
# Tahmin: 75
# <br>
# Durum: Yukari
# <br>
# Tahmin: 87
# <br>
# Durum: Yukari
# <br>
# Tahmin: 93
# <br>
# Durum: Asagi
# <br>
# Tahmin: 90
# <br>
# Durum: Bildin
# </p>

# In[ ]:

import random

print("Sayı tahmin oyunu!")
print("0 ile 100 arasında bir sayı tut ardından program senin sayını tahmin edecek.")

tutulan_sayi = int(input("Aklından bir sayı tut (0-100 arası): "))
tahmin = 50
alt_sinir = 0
ust_sinir = 100
tahmin_sayisi = 1

while tahmin != tutulan_sayi:
    print(f"Tahmin: {tahmin}")
    
    if tahmin < tutulan_sayi:
        print("Durum: Yukarı")
        alt_sinir = tahmin
        tahmin = (alt_sinir + ust_sinir) // 2
    else:
        print("Durum: Aşağı")
        ust_sinir = tahmin
        tahmin = (alt_sinir + ust_sinir) // 2
    
    tahmin_sayisi += 1

print(f"Tahmin: {tahmin}")
print("Durum: Bildin.")
print(f"{tahmin_sayisi} tahminde doğru sayıyı buldum.")


# # Problem 8 Net Yaş Hesaplayıcı
# 
# Kullanıcının bugünün güncel tarihine kadar yaşadığı ay, gün, yıl süresini hesaplayan bir Python kodu yazınız. (Her ay 30 gün kabul edilmeyecektir. Kodu yazarken hangi ayın kaç gün olduğuna [Şubat ayının 29 gün olduğu yıllar dahil] dikkat edin.)

# In[ ]:


from datetime import date
def yas_hesapla(dogum_tarihi):
    bugun = date.today()
    yas = bugun.year - dogum_tarihi.year - ((bugun.month, bugun.day) < (dogum_tarihi.month, dogum_tarihi.day))
    ay = bugun.month - dogum_tarihi.month
    gun = bugun.day - dogum_tarihi.day
    if gun < 0:
        ay -= 1
        gun += 30
    if ay < 0:
        yas -= 1
        ay += 12
    return f"{yas} yıl, {ay} ay, {gun} gün"

dogum_tarihi = input("Doğum tarihinizi (GG/AA/YYYY) formatında girin: ")
dogum_tarihi = date.fromisoformat(dogum_tarihi.replace('/', '-'))
print("Bugüne kadar yaşadığınız süre: " + yas_hesapla(dogum_tarihi))


# # Problem 9 Tek-Çift
# 
# Kullanıcıdan 'q' tuşuna basana kadar rastgele sayılar alın. Tek olanları bir listeye, çift olanları bir başka listeye büyükten küçüğe sıralanacak şekilde atın. Listeleri ekrana yazdıran bir kod yazın.

# In[ ]:


import random

odd_numbers = []
even_numbers = []

while True:
    num = input("Bir sayı girin ya da 'q' tuşuna basarak çıkış yapın: ")
    if num == 'q':
        break
    num = int(num)
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

even_numbers.sort(reverse=True)
odd_numbers.sort(reverse=True)

print("Çift sayılar: ", even_numbers)
print("Tek sayılar: ", odd_numbers)


#  # Problem 10 Altıgen Çizimi
# 
# Kullanıcıdan altıgenin kaç satırdan oluşacağı ve orta satırında kaç karakter olacağı bilgisini alarak '*' karakteri ile bir altıgen çizin. (For loop kullanabilirsiniz.)

# In[ ]:


n = int(input("Altıgenin kaç satırdan oluşacağını girin: "))
m = int(input("Altıgenin orta satırındaki karakter sayısını girin: "))

for i in range(n):
    if i < n // 2:
        print(" " * (n // 2 - i) + "*" * (2 * i + 1))
    elif i == n // 2:
        print("*" * m)
    else:
        print(" " * (i - n // 2) + "*" * (2 * (n - i) - 1))


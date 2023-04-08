#!/usr/bin/env python
# coding: utf-8

# # Problem 1
# Sözlükleri kullanarak bir telefon rehberi yazın. Bu rehberde kullanıcıya kimin telefonunu görüntülemek istediğini sorun ve kullanıcının girdiği isme göre o kişinin telefon numarasını yazdırın. Proje sonunda elde edeceğiniz çıktı  şuna benzer olmalı:
# 
# 
# Lütfen numarasını öğrenmek istediğiniz kişinin adını girin: Ahmet
# 
# Ahmet isimli kişinin numarası şu şekildedir: 0532 678 13 19

# In[8]:


rehber = {"Ahmet":"05326781319"}
kisi = input("Lütfen numarasini ogrenmek istediginiz kisinin adini giriniz:")
print(kisi + " isimli kisinin numarasi su sekildedir:" + rehber[kisi])


# # Problem 2
# Sözlükleri kullanarak bir şirket çalışanları indeksi oluşturun. Bu isim indeksinde kişilerin isimleri key, kişilerin  memleket, yaş ve görev bilgileri value olmalıdır. Burada kullanacağımız value değerleri liste olmalıdır.
# 
# 
# Daha sonra bir isim sorgulama ekranı gibi kullanıcıya kimin bilgilerini görüntülemek istediğini 
# sorun ve sorgulanan kişinin ekranda gösterilmesini sağlayın. Proje sonunda elde edeceğiniz çıktı şu şekilde olmalı:
# 
# 
# Lütfen bilgilerini görüntülemek istediğiniz çalışanın ismini girin: Mehmet Yağız
# 
# Mehmet Yağız= Memleket: Adana Yaş: 40 Görev: Direktör

# In[10]:


sirket_bilgi = {"Mehmet Yağiz":"Memleket:Adana Yaş:40 Görev:Direktör"}
sorgulanan = input("Lütfen bilgilerini görüntülemek istediğiniz çalışanın ismini girin: ")
print(sorgulanan + "=" + sirket_bilgi[sorgulanan])


# # Problem 3
# 
# 3 öğrenciden oluşan bir öğrenci not sözlüğü oluşturun. Bu sözlükte öğrencilerin notları value olarak bir listede toplansın.
# 
# Kullanıcıya hangi öğrencinin notlarını görmek istediğini sorun. Öğrencinin notu görüntülendiğinde program sonunda şöyle bir çıktı elde etmelisiniz:
# 
# ```
# Lütfen notlarını görmek istediğiniz öğrencinin adını girin: Mehmet
# 
# Mehmet isimli öğrencinin      1.Sınav Notu:72
#                               2.Sınav Notu:66
#                               3.Sınav Notu:48
# Not Ortalaması: 62.0
# 

# In[30]:


not_sor = {
    "Mehmet":[72, 66, 48],
    "Sara": [100, 100, 100]
}
kisi = input("Lütfen notlarını görmek istediğiniz öğrencinin adını girin:")
ortalama = (not_sor[kisi][0] + not_sor[kisi][1] +not_sor[kisi][2])/3
print(
    kisi + " isimli öğrencinin 1.Sınav Notu: " + str(not_sor[kisi][0])+
                              " 2.Sınav Notu: " + str(not_sor[kisi][1]) +
                              " 3.Sınav Notu: " +  str(not_sor[kisi][2]) +
                              " Ortalama: " + str(ortalama)
    
    )


# # Problem 4

# In[ ]:


# 1-  "Bmw, Mercedes, Opel, Mazda" elemanlarına sahip bir liste oluşturunuz.
liste=["bmw", "mercedes", "opel", "mazda"]
# 2-  Liste Kaç elemanlıdır ?
print(len(liste))
# 3-  Listenin ilk ve son elemanı nedir ?
print(liste[0],liste[-1])
# 4-  Mazda değerini Toyota ile değiştirin.
liste[-1]="toyota"
# 5-  Listenin -2 indeksindeki değer nedir ?
print(liste[-2])
# 6-  Listenin ilk 3 elemanını alın.
print(liste[0:3])
# 7-  Listenin son 2 elemanı yerine "Toyota" ve "Renault" değerlerini ekleyin.
liste[2:4]="toyota","renault"
print(liste)
# 8-  Listenin üzerine "Audi" ve "Nissan" değerlerini ekleyin.
liste.append("audi"), liste.append("nissan")
print(liste)
# 9- Listenin son elemanını silin.
liste.pop(-1)
print(liste)
# 10- Liste elemanlarını tersten yazdırınız.
liste.reverse()
print(liste)
# 11- Aşağıdaki verileri bir liste içinde saklayınız. 

      # studentA: Yiğit Bilgi 2010, (70,60,70)
      # studentB: Sena Turan  1999, (80,80,70)
      # studentC: Ahmet Turan 1998, (80,70,90) 
studentA = ['Yiğit','Bilgi',2010,[70,60,70]]

studentB = ['Sena','Turan',1999,[80,80,70]]

studentC = ['Ahmet','Turan',1998,[80,70,90]]


# 12- Liste elemanlarını ekrana yazdırınız.
print(studentA,studentB,studentC)


  
names = ['Ali','Yağmur','Hakan','Deniz']
years = [1998, 2000, 1998, 1987]

# 13-  "Cenk" ismini listenin sonuna ekleyiniz.
names.append("Cenk")
print(names)

# 14-  "Sena" değerini listenin başına ekleyiniz.
names.insert(0,"Sena")
print(names)

# 15-  "Deniz" ismini listeden siliniz.
names.pop(-1)
print(names)

# 16-  "Ali" listenin bir elemanı mıdır ?
"Ali" in names

# 17-  Liste elemanlarını ters çevirin.
names.reverse()
print(names)

# 18-  Liste elemanlarını alfabetik olarak sıralayınız.
names.sort()
print(names)

# 19-  years listesini rakamsal büyüklüğe göre sıralayınız.
years.sort()
print(years)

# 20-  str = "Chevrolet,Dacia" karakter dizisini listeye çeviriniz.
str=["Chevrolet","Dacia"]
type(str)

# 21- years dizisinde kaç tane 1998 değeri vardır ?
print(years.count(1998))

# 22- years dizisinin tüm elemanlarını siliniz.
years.clear()
print(years)


# 23- Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız.
markalar = []

marka = input("marka: ")
markalar.append(marka)

marka = input("marka: ")
markalar.append(marka)

marka = input("marka: ")
markalar.append(marka)

print(markalar)




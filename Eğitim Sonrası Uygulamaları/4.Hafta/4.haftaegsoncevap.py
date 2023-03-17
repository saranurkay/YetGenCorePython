
"""
@author: sara
"""
#1.soru

ogrenciler= {}
for i in range(1,4):
    okul_no=input("Okul Numarasını Giriniz:")
    isim= input("İsim Giriniz:")
    soy_isim= input("Soyisim Giriniz:")
    telefon= input("Telefon Numarası Giriniz:")
    dogum_tarihi= input("Doğum Tarihinizi Giriniz:")
    print(f"{i} tane öğrenci bilgisi alındı.")

    ogrenciler[i] = {
    "No": okul_no,
    "İsim": isim,
    "Soyisim": soy_isim,
    "Telefon": telefon,
    "Doğum Tarihi": dogum_tarihi
    }

print(ogrenciler)

#2.soru-asıkkı

numbers = [5,10,10,15,15,15,20,20,20,20]
unique= []
for j in numbers:
    if j in unique:
        continue
    else:
        unique.append(numbers)

print(numbers)

#2.soru-bsıkkı

numbers = [5,10,10,15,15,15,20,20,20,20]
unique=[]
repeat=[]
for number in numbers:
    if numbers.count(number) ==1:
        unique.append(number)
    else:
        repeat.append(number)
print("Tekrar eden elemanlar", repeat)
print("Tekrar etmeyen elemanlar", unique)

#3.soru

sn1 = {1,2,3,4,5}
sn2 = {4,5,6,7,8}
kesisim1= sn1.intersection(sn2)
print(f"Kesişimleri:{kesisim1}")
fark1= sn1.difference_update(sn2)
print(f"Farkları:{sn1}")
fark2=sn2.difference_update(sn1)
print(f"Farkları:{sn2}")
birlesim=sn1.update(sn2)
print(f"Birleşimleri {sn1}")
birlesim2= sn1.union(sn2)
print(f"Birleşimleri {sn1}")

#4.soru

k = "YetGen Core ile Python Öğreniyorum"
print(k)
print(k.capitalize())
print(k.lower())
print(k.upper())
print(k.swapcase())
print(k.title())
print("------------------------------------")
print(k.endswith("Öğreniyorum"))
print(k.startswith("YetGen"))
print(k.find("ile"))
print(k.index("Python"))
print(k.count("e" and "i"))
print("------------------------------------")
print(k.split(" "))
print(k.strip("Y")) #Değişkenin başından ya da sonundan siler.
print(k.join("Selam")) # Karakter dizilerini belirtilen ayraçla birlikte tek bir string haline getirir.
print(k.islower())
print(k.isalpha())
print(k.isdigit())

print(k.lower().islower())


#1

def dikdortgen_alani(kenar):
    return kenar[0]*kenar[1]

kenarlar=[(3,4),(10,3),(5,6),(1,9)]
alanlar= list(map(dikdortgen_alani,kenarlar))
print(alanlar)

#2

def ucgen_mi(kenarlar):
    a, b, c = kenarlar
    return (a + b > c) and (a + c > b) and (b + c > a)
kenarlar = [(3,4,5),(6,8,10),(3,10,7)]
ucgenler = list(filter(ucgen_mi, kenarlar))
print(ucgenler)

#3

liste = [1,2,3,4,5,6,7,8,9,10]
cift_sayilar = list(filter(lambda x: x % 2 == 0, liste))
from functools import reduce

toplam = reduce(lambda x, y: x + y, cift_sayilar)
print(toplam)

#4

isimler = ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]
soyisimler = ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]

for isim, soyisim in zip(isimler, soyisimler):
    print(isim + " " + soyisim)

#5

liste = ['yetgen', 'core', 'python2', 'programı', '2022', 'basic2']

for eleman in liste:
    try:
        if int(eleman):
            print(eleman)
    except ValueError:
        pass
    
    
#@sara


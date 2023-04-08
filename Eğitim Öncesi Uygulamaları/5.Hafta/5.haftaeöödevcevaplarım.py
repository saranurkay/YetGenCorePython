
#1.soru
def dikUcgenAlaniHesapla(a,b):
    return(a*b)/2
print(dikUcgenAlaniHesapla(120,40))

#2.soru

sayi1 = int(input("1.Sayı : "))
sayi2 = int(input("2.Sayı : "))
 
print(sayi1,"ve",sayi2,"arasındaki asal sayılar:")
 
for sayi in range(sayi1,sayi2 + 1):
   if sayi > 1:
       for i in range(2,sayi):
           if (sayi % i) == 0:
               break
       else:
           print(sayi)

#3.soru

a=int(input("Kaç Saat Çalıştınız:"))

def computerPay(b=10, c=15):
    if a<40:
        print(a*b)
    else:
        print(a*c)

computerPay()

#4.soru
def servis_hesapla(arkadas_sayisi):
    servis_sayisi = arkadas_sayisi // 4  # bölümün tam kısmı servis sayısını verir
    kalan = arkadas_sayisi % 4  # kalan arkadaş sayısı
    if kalan > 0:
        servis_sayisi += 1  # kalan arkadaşlar için ek bir servis kiralanması gerekir
    return servis_sayisi
servis_hesapla(15)

#5.soru

toplam = 0 

sayiTopla = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  
  
for ele in range(0, len(sayiTopla)): 
    toplam = toplam + sayiTopla[ele] 
  
print(toplam)


#6.soru

list = [("xxx",1),("xxx",2),("xxx",9),("xxx",3), ("xxx",1),("xxx",13),("xxx",26),("xxx",4)]
print( list[0] , list[4] , list[1] , list[3] , list[-1] , list[2] , list[5] , list[6] )


#7.soru

çiftsayılar=[]
for i in range(1,100):
    if i%2==0:
        çiftsayılar.append(i)
print(çiftsayılar)

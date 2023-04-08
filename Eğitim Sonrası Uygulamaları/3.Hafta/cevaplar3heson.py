
#1.soru

sayi = int(input("Bir sayı giriniz : "))
if sayi > 0:
    print(f"{sayi} sayısı 0'dan büyüktür.")    
elif sayi < 0:
    print(f"{sayi} sayısı 0'dan küçüktür.")
else:
    print(f"{sayi} sayısı 0'a eşittir.")
    
    
#2.soru

sayi = int(input("Bir sayı giriniz :"))
toplam = 0
for i in range(1, sayi):
    if sayi % 1 == 0:
        toplam += 1
if toplam == sayi:
    print("Mükemmel sayı")
else:
    print("Mükemmel sayı değil")


#3.soru

sayi = int(input("Bir sayı giriniz: "))
basamak = str(sayi)
toplam = 0
for x in basamak:
    rakam = int(x) ** len(basamak)
    toplam += rakam
if toplam == sayi:
    print("Armstrong sayı")
else:
    print("Armstrong sayı değildir.")
    
    
#4.soru

for i in range(1, 11):
    for j in range(0, 11):
        print(f"{i} * {j} = {i*j}", end="\t")
    print("")


#5.soru

toplam = 0
while True:
    secim = input("Çıkmak için 'q' diğer durumlarda sayı giriniz: ")
    if secim == "q":
        print("Uygulama sonlandırıldı.")
        break
    else:
        sayi = int(secim)
        toplam += sayi
print(toplam)


#6.soru

for sayi in range(1,101):
    if sayi % 3 == 0 and sayi % 5 == 0:
        print("YetGen")
    elif sayi % 3 == 0:
        print("Yet")
    elif sayi % 5 == 0:
        print("Gen")
    else:
        print(sayi)

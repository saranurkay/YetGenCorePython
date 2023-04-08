
#1

def ciftMi(liste):
    for i in liste:
        if i % 2 == 0:
            print(i,end=" ")
        else:
            raise ValueError("Listenin içerisinde tek sayı var..")
            
            
myList = [2,4,6,8,10,12]

ciftMi(myList)

#2

import random
import time

randomSayi = random.randint(1,100)
oyunHakkı = 5

while True:
    kullanıcıTahmini = int(input("Lütfen sayı tahmininizi giriniz: "))
    
    if kullanıcıTahmini < randomSayi:
        print("Bilgiler işleniyor...")
        time.sleep(2)
        print("Lütfen daha büyük bir tahminde bulununuz.")
        oyunHakkı -= 1
    elif kullanıcıTahmini > randomSayi:
        print("Bilgiler işleniyor...")
        time.sleep(2)
        print("Lütfen daha küçük bir tahminde bulununuz.")
        oyunHakkı -= 1
    elif kullanıcıTahmini == randomSayi:
        print("Bilgiler işleniyor...")
        time.sleep(2)
        print("Tebrikler kazandınız... ")
        oyunHakkı -= 1
        break
    
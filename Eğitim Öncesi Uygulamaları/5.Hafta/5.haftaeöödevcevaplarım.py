
"""

@author: sara
"""

#1.soru


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

#4.soru


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

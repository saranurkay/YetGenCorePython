#!/usr/bin/env python
# coding: utf-8

# # Problem 1
# 
# Fizikte, bir nesnenin sabit ivmeyle hareket ederken son hızını 
# (veya hızını) bulmak için aşağıdaki denklem kullanılabilir:
# ```
# vf = vi + at
# burada:
# vf= son hız
# vi= ilk hız
# a= hızlanma
# t= zaman
# ```
# İlk hız, ivme ve zaman verildiğinde, son hızı döndürecek bir fonksiyon yazın.

# In[ ]:


vi = float(input("ilk hız degerini giriniz: "))
a = float(input("ivme degerini giriniz: "))
t = float(input("zaman degerini giriniz: "))

def sonHiz (vi,a,t):
    vf = float(vi+a*t)
    
    print("son hız:" , vf)
    
sonHiz(vi,a,t)


# # Problem 2
# 
# 1'den 1000'e kadar olan sayılardan mükemmel sayı olanları ekrana yazdırın. Bunun için bir sayının mükemmel olup olmadığını dönen bir tane fonksiyon yazın.
# 
# Bir sayının bölenlerinin toplamı kendine eşitse bu sayı mükemmel bir sayıdır. Örnek olarak 6 mükemmel bir sayıdır (1 + 2 + 3 = 6).

# In[ ]:


def mukemmel_mi(sayi):
    toplam = 0
    for i in range(1,sayi):
        if (sayi % i == 0):
            toplam += i
            
    return toplam == sayi

for i in range(1,1000):
    if (mukemmel_mi(i)):
        print("Mükemmel sayı" , i)


# # Problem 3
# 
# 1'den 100'e kadar olan sayılardan pisagor üçgeni oluşturanları ekrana yazdıran bir fonksiyon yazın.(a <= 100,b <= 100)
# 

# In[ ]:


def pisagor_bulma():
    pisagor_listesi = list()
    
    for i in range(1,101):
        for j in range(1,101):
            c = (i**2 + j **2) ** 0.5
            if (c== int(c)):
                pisagor_listesi.append((i,j,int(c)))
    return pisagor_listesi
for i in pisagor_bulma():
    print(i)




# # Problem 4
# 
# Bir duvar boyamaya karar verdiniz. Boya kutusunun üzerindeki talimatta, 1 kutu boyanın 5 metrekarelik bir duvarı boyayabileceği yazıyor. Rastgele bir duvar yüksekliği ve genişliği verildiğinde, kaç kutu boya satın almanız gerektiğini hesaplayın.
# 
# kutu sayısı = (duvar yüksekliği * duvar genişliği) ÷ kutu başına kaplama.
# 
# örneğin Yükseklik = 2, Genişlik = 4, Kaplama = 5
# 
# kutu sayısı = (2 * 4) ÷ 5 = 1.6
# 
# Ancak bir kutu boyanın 0,6'sını satın alamayacağınız için, sonuç 2 kutuya yuvarlanmalıdır .
# 

# In[ ]:


def kutuBoya(genislik, yukseklik):
    kaplama = 5
    kutuSayısı = genislik * yukseklik / kaplama
    
    if (type(kutuSayısı == float)):
        kutuSayısı = int(kutuSayısı)
        kutuSayısı += 1
    print( "ihtiyacınız olan kutu sayısı: " , kutuSayısı)
    
kutuBoya(4,2)



# # Problem 5
# 
# Bir kelimedeki ünlü ve ünsüz harfleri sayan bir fonksiyon yazınız.

# In[ ]:


def count(val):
    vov = 0
    con = 0
    
    for i in range(len(val)):
        if val[i] in ['a','e','i','o','u']:
            vov = vov+1
            
        else:
            con=con+1
            
    print("Ünlü harf sayısı: ", vov)
    print("Ünsüs harf sayısı: ", con)
    
x = input("Ünlü ve ünsüz harf sayısını öğrenmek için bir kelime yazınız: ")

print(x)
count(x)



# # Problem 6
# 
# Verilen bir listeden çift sayıları yazdıran bir fonksiyon yazınız.
# 

# In[ ]:


def find_even(liste):
    enum = []
    
    for number in liste:
        if number % 2 ==0:
            enum.append(number)
            
    print(enum)
    
list_of_numbers = [1,2,3,4,5,6,7,8,9,10,12]

find_even(list_of_numbers)


# # Problem 7
# 
# 0'dan 10'a kadar olan sayıların toplamını hesaplayan özyinelemeli (Recursive Function) bir fonksiyon oluşturan bir fonksiyon yazınız.
# 
# Özyinelemeli (Recursive Function) bir işlev, kendini tekrar tekrar çağıran bir işlevdir.

# In[ ]:


def toplam(n):
    if n ==0:
        return 0
    else:
        return n + toplam(n-1)
print(toplam(11))



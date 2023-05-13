import numpy as np
array = np.array([23,101,45,86,11])
array.sort()
print(array)

#---------------------------------------------

import numpy as np
Series = np.array([10,15,30,45,60])
print(Series)
Series1 = np.arange(5,15)
print(Series1)

Series2 = np.arange(50,100,5)
print(Series2)

Series3 = np.zeros(10)
print(Series3)

Series5 = np.ones(10)
print(Series5)

Series6 = np.linspace(0,100,5)
print(Series6)

Series7 = np.random.randint(10,30,5)
print(Series7)

Series8 = np.random.uniform(-1,1,10)
print(Series8)

Matris = np.random.randint(10,50, size=(3,5))

satirToplam = np.sum(Matris, axis=1)
sutunToplam = np.sum(Matris, axis=0) 
print("Satır Toplamı: ", satirToplam)  
print("Sütun Toplamı: ", sutunToplam )

matrisMax = np.max(Matris) 
matrisMin = np.min(Matris)
print("En büyük değer: ", matrisMax)  
print("En küçük değer: ", matrisMin )

print(np.argmax(Matris))

Series9 = np.random.randint(10,20, size=7)
print(Series9[:3])

print(Series9[::-1]) 

print(Matris[0])

print(Matris[1,2])

print(Matris[:,0])

print(Matris**2)

Matris = np.random.randint(-50, 50, size=(3,5))
print((Matris > 0) & (Matris % 2 == 0))

#@sara

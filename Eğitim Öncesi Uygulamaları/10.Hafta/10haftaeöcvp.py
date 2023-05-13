#sara
import numpy as np
a = np.array([1,2,3,4,5,6,7,8,9,10])
multi = a.reshape(2,5)
print(multi)
print(multi.shape)
newMatrix = multi.reshape(5,2)
print(newMatrix)
print(multi.ndim)

#----------------------------------------

S = np.arange(1, 10, 2).reshape(3, 3)
S1 = S[:2, :2]
S2 = S[:2, 2:]
S3 = S[2:, :2]
S4 = S[2:, 2:]
B1 = np.concatenate((S1, S2), axis=1)
B2 = np.concatenate((S3, S4), axis=1)
B = np.concatenate((B1, B2), axis=0)
print(B)

#----------------------------------------

a = np.arange(5, 100, 2)
print(a)


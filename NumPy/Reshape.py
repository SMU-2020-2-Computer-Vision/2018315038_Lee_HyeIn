import numpy as np

a = np.array([[1,2,3],[4,5,6]])
print(a)
print("a.shape: ",a.shape)

b = a.ravel()
print(b)

c  = a.reshape(3,2)
print(c)

d = a.T
print(d)

print(a.shape)

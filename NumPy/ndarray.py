import numpy as np


a = np.array([2, 3, 4])
print(a)                
print(type(a))         
print(a.ndim)           
print(a.shape)         
print(a.size)           
print(a.itemsize)       
print(a.nbytes)         
print(a.dtype)         


b = np.array((1.2, 3.5, 5.1, 4.7))
print(b)                
print(type(b))         
print(b.ndim)           
print(b.shape)         
print(b.size)           
print(b.itemsize)       
print(b.nbytes)        
print(b.dtype)       


c = np.array([[1, 2, 3], [4, 5, 6]], dtype='float32')
print(c)                                
print(type(c))         
print(c.ndim)          
print(c.shape)         
print(c.size)          
print(c.itemsize)      
print(c.nbytes)         
print(c.dtype)          


d = np.array([[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]])
print(d)               
print(type(d))          
print(d.ndim)          
print(d.shape)         
print(d.size)          
print(d.itemsize)      
print(d.nbytes)        
print(d.dtype)   
#check dimension of array with ndim Attribute
import numpy as np
a = np.array(40)
b = np.array([40,50,60,70])
c = np.array([[60,70,80],[100,110,120]])
d = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)
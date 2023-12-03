#converting data type on existing array
# astype() function creates the copy of the array and allow you to specify the parameter to it
import numpy as np
arr = np.array([1.1,2.1,3.1])
newarr = arr.astype('i')
print(newarr)
print(newarr.dtype)
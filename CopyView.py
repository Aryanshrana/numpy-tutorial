# copy makes new array and view makes changes to original array
import numpy as np
arr = np.array([1,2,3,4,5])
carr = arr.copy()
varr = arr.view()

varr[0] = 54
carr[0] = 45

print(varr)
print(carr)
print(arr)
# varr and arr will be same

# to check who owns the data or not
# we use base function
print(varr.base)
print(carr.base)
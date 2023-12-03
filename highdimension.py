# create an array with high dimension with ndmin and verify the dimension
import numpy as np
arr = np.array([[100,200,300,400]],ndmin = 5)
print(arr.ndim)
print(arr)
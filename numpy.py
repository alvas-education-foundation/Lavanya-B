""" 

3*3 numpy array
"""

import numpy as np

# Create an array of rank 2
my_arr = np.array([[[1,2,3], [4,5,6],[7,8,9]],[[10,11,12],[13,14,15],[16,17,18]],[[19,20,21],[22,23,24],[25,26,27]]])

print(my_arr)
print(my_arr[1, 2, 1]) # access a single element
print(my_arr.ndim) 
print(my_arr.shape) # n rows, m columns
print(my_arr.size) # number of elements 
print(type(my_arr)) # element type

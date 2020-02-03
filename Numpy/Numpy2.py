import numpy as np

# arr1 = np.zeros((10,0)) Creates Empty Array if either dimension is 0
arr1 = np.zeros((10,))
arr2 = np.ones((10,))
arr3 = np.full((5,2),41)
arr4 = np.empty((10)) # (10,) == (10)

print(arr1)
print(arr2)
print(arr3)
print(arr4) # Empty fills with 1 => empty == ones

print(np.linspace(1,16))
print(arr1.reshape((5,2)))
print(arr1)

print(arr3.flatten())
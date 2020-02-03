import numpy as np

'''
# Creation
x = np.matrix("1,2,3,4;5,6,7,8;9,10,11,12")
print(x)
print(type(x)) #numpy.matrix

# Shape
print(x.shape) # Without braces

# Number of rows
print(x.shape[0])
# Number of columns

# Size -> number of elements
print(x.size)

# Insert ->  np.insert
# Add rows 
# Add Columns

# Update matrix
'''

A = np.matrix(np.arange(0,20)).reshape(5,4)
B = np.matrix(np.arange(20,40)).reshape(5,4)
# Addition of corresponding element
print(np.add(A,B))

# np.subtract

# Matrix Multiplication
print(np.dot(A.T,B)) #Transpose
print(np.matmul(A.T,B))
print(A.T@B)

# Multiply
# Divide
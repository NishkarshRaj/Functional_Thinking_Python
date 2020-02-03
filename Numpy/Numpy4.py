import numpy as np
x = np.arange(1,10).reshape((3,3))
print(x)

# Sum of all values
# print(type(np.sum(x))) #numpy int

# Sum of all columns => axis = 0
# print(np.sum(x,axis=0)) # Generates sum of all columns

# Create another array of same dimension
y = np.arange(11,20).reshape((3,3))
print(y)

# Add two arrays -> Works only for same shape
# print(np.add(x,y)) 

# Multipliation of 2D array!!! -> 
# Not matrix multiplication but of same size arrays => Corresponding
print(np.multiply(x,y))

# subtract
# divide
# remainder

# Slicing Accessing [a:b , x:y] -> if row/column left blank -> take all
# [,] == [:,:]
# Without comma, row specification only

# Subset
# x_sub = x[:2,:2]
# print(x_sub)

# Update Array

# Transpose -> np.transpose()
#print(x.transpose())

# Append -> axis 0 is row here!!!
# np.append([list],axis=0)
# For column, need axis = 1 and reshape to n,1
# np.append(x,[2,2,2],axis=0)
# print(x)

# insert
# np.insert(array,pos,values,axis)
# x_ins =  np.insert(x,1,[41,41,41],axis=0)
# print(x_ins)

# Delete
# np.delete(array, index, axis=0)
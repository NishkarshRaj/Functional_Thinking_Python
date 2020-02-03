# Matrix in Numpy

## Table of contents

1. Create Matrices
2. Dimensions
3. Modifying matrices
4. Accessing elements of a matrix
5. Matrix Operations

**Matrices in Python:** 2D arrays in rows and columns

**1. Creating Matrix**
```Python
mat = np.matrix("1,2,3 ; 4,5,6 ; 7,8,9") # 3x3 matrix -> Use semicolons and ""
```

**2. Dimensions:**  Shape of Matrix
* mat.shape: result in tuple (row,column)
* Number of rows: mat.shape[0]
* Number of columns: mat.shape[1]
* Number of elements: mat.size
* Type of object: numpy.matrix

**3. Modifying matrix**
-> Insert function

np.insert(matrix, index, values, axis)

* No need to reshape for columns unlike in arrays

-> Indexing

4. Accessing elements of array 

-> Indexing 

5. Matrix Operations

5.1) Addition -> similar to array addition, element wise

* Syntax: np.add(mat1,mat2) # add is also used for arrays

BCD!! Matrix creation using arange for arrays: Both of the following ways work

print(np.matrix(np.arange(1,10)).reshape((3,3)))

print(np.matrix(np.arange(1,10).reshape((3,3))))

5.2) Subtract: np.subtract(A,B)

5.3) Element wise multiplication: np.multiply(A,B) -> Same dimension

5.4) Matrix Multiplication/ Dot product: 

> Remember the basic shape condition for matrix multiplication: n*p and p*m => n*m

Way 1: np.dot(A,B)
Way 2: np.matmul(A,B)
Way 3: A@B

5.5) np.divide(A,B)

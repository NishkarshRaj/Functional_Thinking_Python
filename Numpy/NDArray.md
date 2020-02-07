# N-Dimensional Arrays

## Table of Contents

1. Numpy 
2. Creating an Array
3. Generate Arrays using built in functions
4. Advantages of Numpy

**1. Numpy:** Numerical Python

It is a package of pre-defined functions to perform numericals 

**Object:** ndarray (N dimensional Arrays)

**Uses:**
* Mathematical and logical operations on Arrays
* Fourier Transformations
* Linear Algebra -> Rank, Determinants and Solving equations
* Random Number Generation

**2. Creating an Array**

**Syntax:** numpy.array(Object)

**Array:** Ordered and homogeneous

**Type of array:** numpy.ndarray

```Python
print(array) # shows a list type array [] but elements are space separated rather than comma separated in arrays
```

* All elements are coerced into same data type (homogenous)

**3. Generating Arrays using Built in Functions**

**3.1 Linspace**
Creates an array of EQUALLY SPACED elements from start and end

Default number of elements = 50

* **Syntax:** numpy.linspace(start, stop, number of elements, data type, return step)

* Start and stop are both inclusive
* If we want to exclude the end value, use endpoint=False -> Remember if endpoint is not included, does not change the number of elements thus step value changes
* To include the increment value after the array output, use retstep=True

**3.2 arange**

* **Syntax:** numpy.arange(start,stop,step) 

Equally spaced elements decided by step value not the number of values

Here, stop value is exclusive.

**3.3 ones**

* **Syntax:** numpy.ones((Shape in tuple form), Data type)

* Default Data type is float => 1. not 1

**3.4 zeros**

* **Syntax:** numpy.zeros(shape, data type)

Default data type is float => 0. not 0

**3.5 Generate Random Values**

* **Syntax:** numpy.random.rand(shape)

If shape is a single integer, generated 1D array with values ranging in [0,1)

**3.6 Logspace**

Generates equally spaced values based on log value

* **Syntax:** numpy.logspace(start, stop, num, endpoint, base, datatype)

* Default number of elements is 50

* Default base value is 10.0 not 10

* Endpoint if true, include last value (Default value is True)

Scientific Notation -> e+n => base^N

For base 10, generates value from start to stop, i.e., Linspace and logspace work as same when base is 10 for logspace.

For any other base, generates value from base^start to base^stop

**4. Advantages of Numpy**

1. Supports vector operations

2. Arrays are processed in C in backend thus they are faster than Python lists

* Numpy arrays versus Lists in Python.

**1. Speed:** timeit module

```Python
x=range(1000) #list
$ timeit sum(x)
y=numpy.array(x)
$ timeit numpy.sum(y)
```

**2. Size/Memory**

* Memory of Lists (function)

```Python
import sys
sys.getsizeof(x[0])*len(x) //returns size of one element of the list in bytes
-> Memory of Arrays (operator)
y.itemsize * len(y) //itemsize returns size of each element of array in bytes (homogenous)
```

Size maybe less for lists when heterogenous elements:

```Python
import numpy as np
import sys
x = [1,2,3,'str',5]
# print(sys.getsizeof(x[0])*len(x)) # Size is 140
''' But size found above is not correct because heterogenous elements'''
sum=0
for el in x:
    sum = sum + sys.getsizeof(el)
print(sum) # Size is 172
y = np.array(x)
print(y.itemsize*len(y)) # Size is 220
```

<hr>

## Table of Contents

1. Reshaping an array
2. Numpy operations
3. Accessing elements of array

**1. Reshaping an array**

```Python
array1 = array2.reshape(shape) #does not modify old array, creates new array
```

* Creating 1D, 2D and 3D array
* Dimensions

```Python
array.shape -> gives the shape of the array in tuple form, operator not function
```

**2. Numpy Operations:** Element wise operation for same shape arrays

2.1) Addition: numpy.add(arr1,arr2) -> element wise addition of SAME SHAPE array

2.2) Multiplication: numpy.multiply(arr1,arr2) -> element wise multiplication of SAME SHAPE Array => not matrix multiplication 

2.3) numpy.subtract()

2.4) numpy.divide()

2.5) numpy.remainder()

**3. Accessing elements of the array**

Indexing is used: Positive and negative (0-(N-1)) or (-N to -1)

Most important: Accessing elements of 2D arrays -> NOTE!!! array[x][y] and array [x,y] where x defines row and y defines column both works

Generic Accessing 2D array by slicing: array[rstart:rend,cstart:cend]

-> Creation of Subsets of Arrays: By accessing using slicing

-> Updating the array

**BCD!!!!** Updating the subset also updates the original array!!

```Python
import numpy as np
x = np.arange(1,10).reshape((3,3))
subset = x[:2,:2]
subset[0,0]=41
print(subset)
print(x)
```

-> Transpose the array: Does not transpose the original array until assigned back

```Python
* np.transpose(array) # Function
* array.T # Operator
```

-> Append elements to array

* **Syntax:** np.append(array, array to insert, axis)

** Rowise append: axis = 0
** Columnwise append: axis = 1

```Python
import numpy as np
x = np.arange(1,10).reshape((3,3))
'''
# Rowwise Append
row = np.array([[41,41,41]]) # Must be a 2D array of size 1,3 not [41,41,41]
x = np.append(x,row,axis=0)
print(x)
'''
# Columnwise Append
col = np.array([41,41,41]).reshape(3,1)
x = np.append(x,col,axis=1)
print(x)
```

->  Insert

* Syntax: np.insert(array, index, values, axis)

-> Delete entire row/column
* Syntax: np.delete(array, index, axis)

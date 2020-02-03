import numpy as np
import timeit
import sys
'''x = np.array([2,3,'a',4])
print(x)

# Full Linspace coverage
y = np.linspace(start=1,stop=5,num=10,endpoint=True,retstep=True)
print(y)

# Logspace
# numpy.logspace(1,10,num=5, endpoint=True,base=10.0)
print(np.logspace(1,10,num=5, endpoint=True,base=10.0))

# List vs Numpy
x=range(1000)
print(x)
#print(sum(x)) 
# %timeit sum(x) runs only on terminal
y=np.array(x)
# %timeit np.sum(x) runs only on terminal
'''
# Size of list -> sys.getsizeof(object) -> one element
sys.getsizeof(x[0])*len(x)
# Size of Numpy -> ndarray.itemsize -> one element
np.y.itemsize*len(y)
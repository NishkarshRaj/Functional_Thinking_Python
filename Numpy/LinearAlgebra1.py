'''
1. Determinant
2. Rank of Matrix
3. Inverse of Matrix
4. Solving system of equations
'''
'''
import numpy as np

x = np.matrix("2,1,2;1,0,1;3,1,3")

print(np.linalg.det(x))

print(np.linalg.rank(x))

print(np.linalg.inv(x))
'''

import numpy as np

# Solving Linear Equation
A = np.matrix("3,1,2;3,2,5;6,7,8")
x = np.matrix("'x','y','z'").reshape(3,1) # Or Transpose
B = np.matrix("2,-1,3").reshape(3,1) # Or Transpose
# inv A * B
x = np.linalg.solve(A,B)
print(x)

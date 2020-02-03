# Linear Algebra

## Table of Contents

1. Determinant of Matrix
2. Rank of Matrix
3. Inverse of Matrix
4. Solving system of equations

**1. Determinant**

Condition: Square Matrix

Used for: Inverse and Solving set of equation

* Syntax: numpy.linalg.det(matrix)

**2. Rank of Square matrix:** Number of linearly independent variables k in n*n matrix where k<=n

Used: Machine Learning

* Syntax: numpy.linalg.matrix_rank(matrix)

**3. Inverse of Matrix** (Multiplicative Inverse)


**Ainv = Aadjoint/det(A)**

* Syntax: numpy.linalg.inv(matrix)

BCD!! If determinant of matrix is 0 -> singular matrix -> Inverse does not exists

**4. Solving system of Equation**

N independent variables and N equations are given in form of 

A*X = B

We have to find X

X = Ainv * B

BCD! There can be three possibilities:

A) No solutions

B) Exactly N solutions

C) Infinite solutions

**Shortcut method:** np.linalg.solve(A,B)

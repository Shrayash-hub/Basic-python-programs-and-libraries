# using numpy to perform operations on 2d matrix
import numpy as np

A = np.array([[5,6],
              [7,8]])

B = np.array([[1,2],
              [3,4]])

C = A + B
print("Matrix A + B:\n", C)

#matrix multiplication
D = np.dot(A,B)
print("\nMatrix A*B (Dot Product):\n", D)

# Transpose
E = A.T

# Determinant of a matrix
det_A = np.linalg.det(A)
print("\nDeterminant of A:\n", det_A)

# Inverse of a matrix (if it exists)
if det_A !=0:
  A_inv = np.linalg.inv(A)
  print("\nInverse of A:\n", A_inv)
else:
  print("\nInverse of A does not exist (singular matrix)")

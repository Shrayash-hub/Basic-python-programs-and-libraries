import numpy as np

# creating an array from a list
arr1 = np.array([1,2,3,4,5])
print("Array created fro list:",arr1)

#creating an array of zeros
arr_zeros = np.zeros(5)
print("Array of zeros:",arr_zeros)

#creating an array of ones
arr_ones = np.ones(5)
print("Array of ones:",arr_ones)

#creating a 2d indetity matrix
identity_matrix = np.eye(3)
print("Wd Identity Matrix:\n",identity_matrix)

#creatting an array with a range of values
arr_range = np.arange(0,10,2) # 0 is inclusive and 10 is exclusive
print("Array with range of values:",arr_range)

#Creating a random array of shape(2,3)
arr_random = np.random.rand(2,3)
print("Random array of shape (2,3):\n",arr_random)

# performing operations on vectors using numpy 

import numpy as np

#Define two vectors
v1 = np.array([3,4])
v2 = np.array([1,2])

#vector Addition
v_add = v1+v2
print("Vector Addition (v1+v2):", v_add)

#vector Subtraction
v_sub = v1-v2
print("Vector Subtraction (v1-v2):", v_sub)

#vector dot product
v_dot = np.dot(v1,v2)
print("Vector dot product: ",v_dot)

#vector cross product -> we need 3d vectors
v1_3d = ([[1,2,3],
          [5,6,7],
          [8,9,10]])
v2_3d = ([[0,9,8],
          [7,6,5],
          [4,3,2]])

v_cross = np.cross(v1_3d,v2_3d)
print("Vector cross product: ",v_cross)

v1_mag = np.linalg.norm(v1_3d)
v2_mag = np.linalg.norm(v2_3d)
print("Magnitude of v1: ",v1_mag)
print("Magnitude of v2: ",v2_mag)

cos_angle = v_dot / (v1_mag * v2_mag)
print("cos_angle:",cos_angle)

cos_angle = np.clip(cos_angle, -1.0, 1.0)
    
# Calculate angle
angle = np.arccos(cos_angle)
    
# Convert to degrees if requested
print(np.degrees(angle))


import numpy as np

# ndim attribute

arr1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(f"arr1 :\n{arr1}")
print(f"Dimension :{arr1.ndim}")

print("-" * 60)

# size attribute
arr2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(f"arr2 :\n{arr2}")
print(f"Array Size :{arr2.size}")

print("-" * 60)
# shape attribute

arr3 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(f"arr3 :\n{arr3}")
print(f"Array Shape :{arr3.shape}")

print("-" * 60)
# dtype attribute

arr4 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(f"arr4 :\n{arr4}")
print(f"Array Dtype :{arr4.dtype}")


print("-" * 60)
# itemsize attribute - size of each element in bytes

arr5 = np.array([[1, 2, 3], [5, 6, 7]])
print(f"arr5 :\n{arr5}")
print(f"Array Itemsize :{arr5.itemsize}")

print("-" * 60)
# attribute data

arr6 = np.array([[1, 2, 3], [5, 6, 7]])
print(f"arr6 :\n{arr6}")
print(f"Array data :{arr6.data}")

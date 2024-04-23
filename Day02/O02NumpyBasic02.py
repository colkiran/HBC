
import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
print(f"arr1 :{arr1}")
print(f"Datatype  :{arr1.dtype}")
print(f"Dimension :{arr1.ndim}")

print("-" * 60)
arr2 = np.array([-2, -1, 0 , 1, 2])
print(f"arr2 :{arr2}")
print(f"Datatype  :{arr2.dtype}")
print(f"Dimension :{arr2.ndim}")

print("-" * 60)
arr3 = np.array([0.1, 0.2, 0.3])
print(f"arr3 :{arr3}")
print(f"Datatype  :{arr3.dtype}")
print(f"Dimension :{arr3.ndim}")

print("-" * 60)
arr4 = np.array([1+2j, 2+3j, 3+4j])
print(f"arr4 :{arr4}")
print(f"Datatype  :{arr4.dtype}")
print(f"Dimension :{arr4.ndim}")

print("-" * 60)
arr5 = np.zeros((3, 3), dtype='int32')
print(f"arr5 :\n{arr5}")
print(f"Datatype  :{arr5.dtype}")
print(f"Dimension :{arr5.ndim}")

print("-" * 60)
# 8 bit integer
arr1 = np.array([10, 20, 30], dtype='int8')
print(f"arr1 :{arr1}")
print(f"Dtype :{arr1.dtype}")

print("-" * 60)
# 16 bit array
arr2 = np.array([2, 4, 6, 8], dtype='uint16')
print(f"arr2:{arr2}")
print(f"Dtype :{arr2.dtype}")

print("-" * 60)
# float 32 bit
arr3 = np.array([2.1, 3.2, 4.3, 5.4], dtype='float32')
print(f"arr3: {arr3}")
print(f"Dtype :{arr3.dtype}")

print("-" * 60)
arr4 = np.array([1-2j, 2-3j, 3-4j], dtype='complex64')
print(f"arr :{arr4}")
print(f"Dtype :{arr4.dtype}")

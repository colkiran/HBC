
import numpy as np
# Broadcasting

arr1 = np.array([1, 2, 3])
print(f"arr1 :{arr1}")

arr2 = np.array([[1], [2], [3]])
print(f"arr2 :{arr2}")

res = arr1 + arr2
print(f"res :{res}")

print("-" * 60)

arr1 = np.array([1, 2, 3, 4, 5, 6, 7])
arr2 = np.array([8, 9, 10, 11, 12, 13, 14])

res = arr1 * arr2
print(f"res :{res}")

print("-" * 60)

# arr1 = np.array([1, 2, 3, 4, 5, 6, 7])
# arr2 = np.array([8, 9, 10, 11, 12, 13, 14, 15])
#
# res = arr1 * arr2
# print(f"res :{res}")

a = np.array([[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12]])

print(f"array :\n{a}")

b = [2, 2, 2, 2]
print(f"array :{b}")

print(a + b)




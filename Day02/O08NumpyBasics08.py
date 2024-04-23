
import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
print(f"arr1 :{arr1}")

n = 10
res = arr1 + n
print(f"res :{res}")

print("-" * 60)

arr1 = np.array([[1, 2, 3],
                 [4, 5, 6]])

arr2 = np.array([[1, 2, 1],
                 [1, 2, 1]])

print(f"arr1 :\n{arr1}")
print(f"arr2 :\n{arr2}")

arr3 = arr1 + arr2
print(f"arr :\n{arr3}")

print("-" * 60)

arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(f"arr1 :{arr1}")

def get_square(x):
    if x == 0:
        return 0
    else:
        return x ** 2


vector_fun = np.vectorize(get_square)

res = vector_fun(arr1)
print(f"res :{res}")

print("-" * 60)

arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(f"arr1 :{arr1}")

boolean_mask = arr1 > 5
print(f"Boolean Mask :{arr1 > 5}")

print(arr1[boolean_mask])

print("-" * 60)
boolean_mask = arr1 % 2 == 1
print(arr1[boolean_mask])

arr2 = np.array([1, 2, 4, 9, 11, 16, 18, 22, 26, 31, 32, 47, 51])
print(f"arr2 :{arr2}")

boolean_mask = (arr2 < 10) | (arr2 > 35)
print(arr2[boolean_mask])

print("-" * 60)

arr2 = np.array([1, 2, 4, 9, 11, 16, 18, 22, 26, 31, 32, 47, 51, 52])
print(f"arr2 :{arr2}")

#arr1 = arr2                 # shallow copy
arr1 = arr2.copy()          # deep copy

arr1[arr1 % 2 == 0] = 0
print(f"arr1 :{arr1}")
print(f"arr2 :{arr2}")


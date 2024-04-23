
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(f"arr :{arr}")

print("-" * 60)
# reshape

arr1 = arr.reshape([2, 6])
print(f"arr1 :\n{arr1}")

print("-" * 60)
arr2 = arr.reshape([3, 4])
print(f"arr2 :\n{arr2}")

print("-" * 60)
arr3 = arr.reshape([2, 3, 2])
print(f"arr3 :\n{arr3}")

print("-" * 60)
arr4 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(f"arr4 :\n{arr4}")

print("-" * 60)
# iteration

for x in arr4:
    print(x)

print("-" * 60)

for x in arr4:
    for y in x:
        print(y)
    print("-" * 60)

print("-" * 60)

for x in arr4:
    for y in x:
        for z in y:
            print(z)
    print("-" * 60)

print("-" * 60)

for x in np.nditer(arr4):
    print(x)

print("-" * 60)

arr1 = np.array([3, 6, 4, 2, 8, 5, 1, 7])
print(f"arr1 :{arr1}")

# sort the array
res = arr1[np.argsort(arr1)]
print(f"res :{res}")

print("-" * 60)

# sort in descending order
res = arr1[np.argsort(-arr1)]
print(f"res :{res}")


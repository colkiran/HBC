
import numpy as np

arr1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(f"arr1 :\n{arr1}")
np.save("myfile.npy", arr1)

print("-" * 60)
# load the data from a file
arr2 = np.load("myfile.npy")
print(f"arr2 :\n{arr2}")

print("-" * 60)
# save the array into a text file

arr1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(f"arr1 :\n{arr1}")
np.savetxt("myfile.txt", arr1)

print("-" * 60)
# load data from a text file

# arr2 = np.loadtxt("myfile.txt", dtype='int32')    - deprecated
arr2 = np.loadtxt("myfile.txt").astype(np.int64)
print(f"arr2 :\n{arr2}")




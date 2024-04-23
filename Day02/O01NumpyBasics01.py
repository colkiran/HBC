
import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])

print(f"arr1 :{arr1}")

print(type(arr1))

print(f"Numpy Version :{np.__version__}")

print("-" * 60)

print("Zero Dimension".center(60, "-"))
arr0 = np.array(50)
print(f"arr0 :{arr0}")
print(f"Dimension :{arr0.ndim}")

print("One Dimension".center(60, "-"))
arr1 = np.array([1, 2, 3, 4, 5])
print(f"arr1 :{arr1}")
print(f"Dimension :{arr1.ndim}")

print("Two Dimension".center(60, "-"))
arr2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(f"arr2 :\n{arr2}")
print(f"Dimension :{arr2.ndim}")

print("Three Dimension".center(60, "-"))
arr3 = np.array([[[1, 2, 3],[4, 5, 6]],[[7, 8, 9], [10, 11, 12]]])
print(f"arr3 :\n{arr3}")
print(f"Dimension :{arr3.ndim}")

print("-" * 60)
arr4 = np.array([1, 2, 3, 4, 5], ndmin = 5)
print(f"arr4 :{arr4}")
print(f"Dimension :{arr4.ndim}")

print("-" * 60)
arr5 = np.zeros((2, 3))
print(f"arr5 :\n{arr5}")

print("-" * 60)
arr6 = np.zeros((2, 3, 4))

print(f"arr6 :\n{arr6}")

print("-" * 60)
arr7 = np.ones((3, 3))
print(f"arr7 :\n{arr7}")

print("-" * 60)
arr8 = np.full((3, 3), 5)
print(f"arr8 :\n{arr8}")

print("-" * 60)
arr9 = np.random.rand(2, 2, 2)
print(f"arr9 :{arr9}")

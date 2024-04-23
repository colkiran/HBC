
import  numpy as np
# add

arr1 = np.array(['iphone :', "price :"])
arr2 = np.array(['15', '129000'])

print(f"arr1 :{arr1}")
print(f"arr2 :{arr2}")

print("-" * 60)
res = np.char.add(arr1, arr2)
print(f"res :{res}")

print("-" * 60)
# multiply
arr1 = np.array(['A', 'B', 'C'])
print(f"arr1 :{arr1}")

res = np.char.multiply(arr1, 2)
print(f"res :{res}")

print("-" * 60)
cities = np.array(['bangalore', 'CHENNAI', 'delhi', 'mumbai', 'HYDERABAD', 'thiruvananthapuram'])

print(f"cities :{cities}")
res = np.char.capitalize(cities)
print(f"Captilized :{res}")

res1 = np.char.upper(cities)
print(f"res1 :{res1}")

res2 = np.char.lower(cities)
print(f"res2 :{res2}")

print("-" * 60)
cities = np.array(['Bangalore', 'Chennai', 'Hyderabad'])
print(f'cities :{cities}')
res = np.char.join("-", cities)
print(f"res :{res}")

print("-" * 60)
arr1 = np.array(['A', 'B', 'C', 'hello', 'world'])
arr2 = np.array(['A', 'B', 'c', 'hello', 'World'])

print(f"arr1 :{arr1}")
print(f"arr2 :{arr2}")

res = np.char.equal(arr1, arr2)
print(f"res :{res}")

print("-" * 60)

mat1 = np.array([[1, 2],
                [3, 4]])
mat2 = np.array([[6, 7],
                [8, 9]])
print(f"mat1 :\n{mat1}")
print(f"mat2 :\n{mat2}")

# multiply
res = np.dot(mat1, mat2)
print(f"res :\n{res}")

print("-" * 60)

mat1 = np.array([[1, 2],
                 [3, 4]])

mat2 = np.array([[1, 2, 3],
                 [4, 5, 6]])

print(f"mat1 :\n{mat1}")
print(f"mat2 :\n{mat2}")

res1 = np.transpose(mat1)
res2 = np.transpose(mat2)

print(res1)
print(res2)

print("-" * 60)

mat1 = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 6, 9]])

print(f"mat1 :{mat1}")

# inverse
res = np.linalg.inv(mat1)

mat1 = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 9, 8]])

print(f"mat1 :{mat1}")

# inverse
res = np.linalg.inv(mat1)

print(f"res :{res}")

print("-" * 60)

mat1 = np.array([[1, 2],
                 [3, 4]])

mat2 = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 9, 8]])


print(f"mat1 :{mat1}")
print(f"determinent :{np.linalg.det(mat1)}")

print(f"mat2 :{mat2}")
print(f"determinent :{np.linalg.det(mat2)}")

print("-" * 60)

mat1 = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])
print(f"mat1: \n{mat1}")

print(f"mat1 :{mat1.flatten()}")



import pandas as pd

pds = pd.Series()
print(f"Panda Series :{pds}")
print(type(pds))

print("-" * 60)
ps = pd.Series([1, 2, 3, 4, 5])
print(f"Panda Series :\n{ps}")

print("-" * 60)
ps = pd.Series({'a': 'apple', 'b': 'ball', 'c': 'cat', 'd': 'dog', 'e':'elephant'})
print(f"Panda Series :\n{ps}")

print("-" * 60)
ps = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
print(f"Pandas Series :\n{ps}")

print("-" * 60)
ps1 = pd.Series([1, 2, 3, 4, 5])
ps2 = pd.Series([10, 20, 30, 40, 50], index=['aa', 'bb', 'cc', 'dd', 'ee'])
print(f"Series1 :\n{ps1}")
print(f"Series2 :\n{ps2}")

print("-" * 60)
print(f"Index ps1:{ps1.index}")
print(f"Index ps2:{ps2.index}")

print("-" * 60)
print(f"Values ps1 :\n{ps1.values}")
print(f"Values ps2 :\n{ps2.values}")

print("-" * 60)
print(f"Dtype ps1 :{ps1.dtype}")
print(f"Dtype ps2 :{ps2.dtype}")

print("-" * 60)
print(f"Shape ps1 :{ps1.shape}")
print(f"Shape ps2 :{ps2.shape}")

print("-" * 60)
ps3 = pd.Series()
print(f"ps1.empty :{ps1.empty}")
print(f"ps2.empty :{ps2.empty}")
print(f"ps3.empty :{ps3.empty}")

print("-" * 60)
print(f"Count ps1: {ps1.count()}")
print(f"Count ps2: {ps2.count()}")

print("-" * 60)
print(f"Len ps1 :{len(ps1)}")
print(f"len ps2 :{len(ps2)}")


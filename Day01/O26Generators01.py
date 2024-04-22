
l1 = [x ** 2 for x in range(1, 11)]
print(f"l1 :{l1}")
print(type(l1))

print("-" * 60)

l2 = (x ** 2 for x in range(1, 11))
print(f"l2 :{l2}")
print(type(l2))

print("-" * 60)
s1 = sum([x ** 2 for x in range(1, 11)])
print(f"Comprehension :{s1}")

print("-" * 60)
s2 = sum((x ** 2 for x in range(1, 11)))
print(f"Generator :{s2}")

print("-" * 60)
from sys import getsizeof

l1 = [x ** 2 for x in range(10000)]
print(f"Comprehension size of the list :{getsizeof(l1)}")

print("-" * 60)

l2 = (x ** 2 for x in range(10000))
print(f"Generator size of the list :{getsizeof(l2)}")

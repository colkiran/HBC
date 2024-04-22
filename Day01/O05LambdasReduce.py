
from functools import reduce
l1 = [3, 5, 8, 6, 9, 2, 4]
print(f"l1 :{l1}")

res_largest = reduce(lambda x, y: x if x > y else y, l1)
print(f"Largest Number :{res_largest}")

res_smallest = reduce(lambda x, y: x if x < y else y, l1)
print(f"Smallest Number :{res_smallest}")

print("-" * 60)

l1 = list(range(1, 11))
print(f"l1 :{l1}")

res = reduce(lambda x, y: x + y, l1)
print(f"Sum of numbers :{res}")

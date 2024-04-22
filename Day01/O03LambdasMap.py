"""
 Lambdas - anonymous functions with a single expression

 result of the expression = lambda var1, var2,  var3, .....: expression

lambdas are best used with map, filter and reduce

"""

def add(x, y):
    return x + y

a = add

print(a(300, 400))

print("-" * 60)

b = lambda x, y: x + y

print(b(10, 20))

print("map".center(60, "-"))

def add(x, y):
    return x + y

l1 = list(range(1, 11))
print(f"l1 :{l1}")

res = list(map(add, l1, l1))
print(f"res :{res}")


res = list(map(lambda x : x ** 2,l1))
print(f"res :{res}")

print("-" * 60)

months = ['dec', 'oct', 'aug', 'feb', 'apr', 'jan', 'nov', 'mar', 'jun', 'may', 'sep', 'jul']

print(f"months :{months}")
# sort these months by calendar - sort, map

print("-" * 60)
from calendar import month_abbr
print(f"month_abbr : {list(month_abbr)}")

print("-" * 60)
res = sorted(months, key=list(map(lambda month: month.lower(), list(month_abbr) )).index)

print(f"res :{res}")


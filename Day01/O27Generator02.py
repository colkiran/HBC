
def fun():
    x = 1
    print("Ooty apples")
    yield x
    x += 9
    print("Oranges from kanpur")
    yield x
    x += 10
    print("Grapes from Hubli")
    yield x

# print(fun())
gen = fun()
print(gen)

print("-" * 60)
print(gen.__next__())

print("-" * 60)
print(gen.__next__())

print("-" * 60)
print(gen.__next__())

# print("-" * 60)
# print(gen.__next__())


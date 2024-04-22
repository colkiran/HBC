
l1 = ['a', 'b', 'c', 'd']
print(f"l1 :{l1}")
print(type(l1))

# print(dir(l1))
iterObj = l1.__iter__()
print(dir(iterObj))

print("-" * 60)
e1 = iterObj.__next__()
print(e1)
e2 = iterObj.__next__()
print(e2)
e3 = iterObj.__next__()
print(e3)
e4 = iterObj.__next__()
print(e4)
# e5 = iterObj.__next__()
# print(e5)



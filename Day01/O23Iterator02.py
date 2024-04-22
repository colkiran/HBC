
l1 = [1, 2, 3, 4, 5]
print(f"l1 :{l1}")

iterObj = iter(l1)          # l1.__iter__()

while True:
    try:
        elem = iterObj.__next__()
        print(elem, end=" ")
    except StopIteration:
        break
print()

print("-" * 60)

for i in l1:
    print(i, end=" ")



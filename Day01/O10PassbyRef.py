
def fun(lst):
    print(f"lst :{lst}")
    lst.extend([6, 7, 8, 9, 10])
    print(f"lst :{lst}")


l1 = [1, 2, 3, 4, 5]
print(f"l1 before the function call :{l1}")
fun(l1)
print(f"l1 after the function call :{l1}")

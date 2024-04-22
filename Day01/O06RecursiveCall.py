
def fact(x):
    if x == 0:
        return 1
    else:
        return x * fact(x - 1)

n = 5
print(f"The factorial of {n} is :{fact(n)}")


from collections import namedtuple

def ArithmeticCalc(x, y):
    sum = x + y
    diff = x - y
    prod =  x * y
    quot = x / y
    nmdTpl = namedtuple("Arithmetic", "add sub mul div")
    arith = nmdTpl(add = sum, sub = diff, mul = prod, div = quot)
    return arith

res = ArithmeticCalc(20, 8)
print(f"res :{res}")

print(f"Addition        :{res.add}")
print(f"Subtraction     :{res.sub}")
print(f"Multiplication  :{res.mul}")
print(f"Division        :{res.div}")

print("-" * 60)

def fun():
    "this is a docstring"
    # this is a comment
    print("Hello World")

fun()
print(fun.__doc__)

print("-" * 60)

def fun1(x, y):
    """
    function fun1 takes 2 arguments
    1. if both the args are numbers then we get the sum of the numbers
    2. if both the args are strings then we get a concatenated string
    3. if the args are of different data types then it throws an error message
    """

    print(f"x + y = {x + y}")

fun1(10, 20)
fun1("hello ", "world")

print("-" * 60)
help(fun1)

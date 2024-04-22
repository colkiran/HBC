
# any variable declared inside the function is not accessible outside the function

def fun(x):                 # x is a local variable
    print(f"x :{x}")
    y = "hello world"       # local variable
    print(f"y :{y}")

fun(100)
print(f"y :{y}")
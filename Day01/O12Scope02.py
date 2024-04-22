

glbX = 100

def fun(x):                     # x is a local variable
    global glbX                 # do not assign any value in this line
    print(f"x :{x}")
    glbX = 500
    print(f"Inside glbX :{glbX}")


print(f"Before the function call :{glbX}")

fun(150)

print(f"After the function call :{glbX}")

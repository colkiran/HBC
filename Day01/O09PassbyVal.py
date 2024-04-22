
def fun(st):
    print(f"st :{st}")
    st += " world"      # st = st + " world"
    print(f"st :{st}")

st = "hello"
print(f"before the function call :{st}")
fun(st)
print(f"after the function call :{st}")

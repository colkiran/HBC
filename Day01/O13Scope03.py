
def outerFun(gname):
    print(f"before :{gname}")

    def innerFun():
        # only local variables can be stored as nonlocal variables
        nonlocal gname
        gname = gname + " Tendulkar"
        print("Hello World")
        print(f"Greetings {gname}")

    innerFun()
    print(f"after :{gname}")

outerFun("Sachin")
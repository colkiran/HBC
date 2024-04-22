
def outerFun(gname):
    gname = "Mr." + gname

    def innerFun():

        print(f"Greetings {gname}")

    innerFun()

outerFun("Rahul")

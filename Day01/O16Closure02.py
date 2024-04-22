

def outerFun(gname):            # HOF - Higher Order Function
    gname = "Mr." + gname

    def innerFun():

        print(f"Greetings {gname}")

    return innerFun


outerFun("Sachin")()            # calls the inner function

print("-" * 60)

inref = outerFun("Rahul")

# after few lines of code

inref()



def outerFun(greet):

    # simple curry
    def innerFun(gname):

        print(greet, gname)

    return innerFun

engGrt = outerFun("Welcome")
engGrt("Sachin")
engGrt("Messi")

print("-" * 60)
kanGrt = outerFun("Namaskara")
kanGrt("Rahul")
kanGrt("Kumble")

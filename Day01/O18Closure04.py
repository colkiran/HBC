
def outerFun(greet):

    def innerFun(sep):

        def innerMostFun(name):

            from emojis import emojis

            emojized = emojis.encode(greet + " :" + sep + ": " + name)

            print(emojized)

        return innerMostFun

    return innerFun

kanGrt = outerFun("Namaskara")

kanGrtTgr = kanGrt("bear")

kanGrtTgr("Prabhakar")





"""
outerFun("Welcome")("----->")("Sachin")

engGrt = outerFun("Welcome")

engGrtSngArw = engGrt("------>")
engGrtDblArw = engGrt("======>>")

engGrtSngArw("Sachin")
engGrtDblArw("Sehwag")


"""
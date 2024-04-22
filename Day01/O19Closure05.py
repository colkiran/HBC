
def fun(*args):
    print(args)


fun()
print("-" * 60)

fun(10)
print("-" * 60)

fun(1, 2)
print("-" * 60)

fun(1, 2, 3)
print("-" * 60)


def sum(x, y):
    print("Sum fnc called....")
    return x + y

def diff(x, y):
    print("Diff fnc called......")
    return x - y


def login_details(fnc):
    log = "Logging into the service......."

    def helper(*args):
        print(log)
        print(fnc(*args))           # call back
        print("-" * 60)

    return helper


sumRef = login_details(sum)
sumRef(10, 20)

print("-" * 60)

diffRef = login_details(diff)
diffRef(20, 8)



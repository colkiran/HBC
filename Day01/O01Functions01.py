
def greet():
    print("Greetings Mr. Sachin, Welcome to the event.....")

def greetGst(gname):
    print(f"Greetings Mr.{gname}, Welcome to the event.......")

# cty as default argument and gname as non default arg
def greetGstCty(gname, cty="Mumbai"):
    print(f"Greetings Mr.{gname} from {cty}, Welcome to the event.....")

greet()

print("-" * 60)

greetGst("Rahul")

print("-" * 60)

greetGstCty("Sachin")

greetGstCty("Rohit")

greetGstCty("Rahul", "Bangalore")

print("-" * 60)
# varailble length args *args

def MultipleMe(*numbers):
    print(numbers)
    print(*numbers)
    prd = 1
    for number in numbers:
        prd *= number

    return prd

print(MultipleMe(1, 2, 3, 4, 5))

print("-" * 60)

def extractDetails(**details):
    print(details)
    for k, v in details.items():
        print(k + " => " + str(v))

extractDetails(name="Sachin", age=35, runs=150, oppn="Aus", venue='Perth')

print("return".center(60, "-"))

def Multime(x, y):
    return x * y

print(Multime(10, 20))

print("-" * 60)

def ArithmeticCalc(x, y):
    sum = x + y
    diff = x - y
    prod =  x * y
    quot = x / y
    return sum, diff, prod, quot

res = ArithmeticCalc(20, 8)
print(f"res :{res}")

#NamedTuple





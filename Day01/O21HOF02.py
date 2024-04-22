



def outerFun(fnc):

    def helperFun(amount):
        print("Logging into the server......")
        fnc(amount)
        print("Logging out of the server......")
        print("-" * 60)

    return helperFun


@outerFun               # deposit = outerFun(deposit)
def deposit(amt):
    print(f"credited amount {amt} into account ending ####")

@outerFun
def withdraw(amt):
    print(f"amount {amt} debited from account ending ####")


deposit(75000)
withdraw(15000)

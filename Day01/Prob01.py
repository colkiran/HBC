import time

def timeCalc(fnc):

    def helper(itr):
        print("function called.....")
        st = time.perf_counter()
        fnc(itr)
        et = time.perf_counter()
        print(f"time taken to execute {round(et - st, 2)}")
        print("-" * 60)

    return helper

@timeCalc
def fun(num):
    lst = []
    for i in range(num):
        for j in range(1, num+1):
            lst.append(j ** 2)


fun(4500)
# Write code for algorithm 3 below

def fib_num(f):
    if f<= 0:
        print("Lets get some real Fibbonacci numbers! Select something other than 0!")
    elif f == 1:
        return 0
    elif f == 2:
        return 1
    else:
        return fib_num(f-1)+fib_num(f-2)


print(fib_num(2))
print(fib_num(4))
print(fib_num(10))

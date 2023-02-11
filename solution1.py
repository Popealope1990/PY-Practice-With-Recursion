# Write code for algorithm 1 below

def counting(a):
    if a == 0:
        print("Please don't make me count anymore! :'(")
    
    else:
        print(a)
        counting(a-1)

counting(5)
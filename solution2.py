# Write code for algorithm 2 below

def going_up(b, c=1):
    if b<c:
        print("Chuck Norris once counted to infinity! Why are we stoping?")
    else:
        print(c)
        going_up(b, c+1)

going_up(10)
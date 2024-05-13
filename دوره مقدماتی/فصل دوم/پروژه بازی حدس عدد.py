import random


a=1
b=99
rnd=random.randrange(a,b)
print(rnd)
myAnswer=input()
while myAnswer!="d" :
    if myAnswer == "b":
        a=rnd
    elif myAnswer=="k":
        b=rnd
    rnd=random.randrange(a,b)
    print(rnd)
    myAnswer=input()

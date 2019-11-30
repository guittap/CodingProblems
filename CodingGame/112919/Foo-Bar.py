for i in range(int(input())):
    if (i+1)%5>0 and (i+1)%7>0:print(i+1,end="")
    if (i+1)%5==0:print("Foo",end="")
    if (i+1)%7==0:print("Bar",end="")
    print("")
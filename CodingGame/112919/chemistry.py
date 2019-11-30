import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
c = 0
h = 0
for i in range(n):
    line = input()
    for i in line:
        if i == 'C':
            c+=1
        elif i=='H':
            h+=1

if c==1 and h==4:
    print("methane")
    
elif c==2 and h==6:
    print("ethane")

elif c==3 and h==8:
    print("propane")
    
elif c==4 and h==10:
    print("butane")
    
elif c==5 and h==12:
    print("pentane")
    
else:
    print("NONE")
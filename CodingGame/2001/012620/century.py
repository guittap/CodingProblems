import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

y = int(input())

if y<0:
    y = math.floor(y/100)*-1
    print(str(y), "st" if str(y)[-1] == "1" else "nd" if str(y)[-1] == "2" else "rd" if str(y)[-1] == "3" else "th", " century BCE", sep="")
elif y>0:
    y =  math.ceil(y/100)
    print(str(y), "st" if str(y)[-1] == "1" else "nd" if str(y)[-1] == "2" else "rd" if str(y)[-1] == "3" else "th", " century CE", sep="")
else: 
    print("INVALID")

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

s = input()

b=0
a=""
for i in s:
    if i==' ':
        a+=i
        b=0
    elif b==0:
        a+=i.upper()
        b+=1
    else:
        a+=i.lower()
        b+=1
        
    
print(a)
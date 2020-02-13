import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

k = input()
if len(k)%2==0:
    a=k[0:len(k)//2]
    b=k[len(k)//2:]
    
    
    print(a[::-1]+b[::-1])
else:
    a=k[0:len(k)//2]
    b=k[len(k)//2+1:]
    print(a[::-1]+k[len(k)//2]+b[::-1])
import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
a = 0

for i in range(1,n+1,1):
    if i%7==0:
        a+=1
    elif "7" in str(i):
        a+=1
    elif sum(int(x) for x in str(i))%7==0:
        a+=1
        
print(a)
import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = input()
last = n[0]
count = 0

for i in n:
    if i!=last:
        print(str(count)+last,end="")
        count = 0
    last = i
    count +=1
        
print(str(count)+last,end="")
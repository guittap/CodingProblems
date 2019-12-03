import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
list = []

for i in range(int(n**.5)):
    if n%(i+1)==0:
        list.append(i+1)

if len(list) < 2:
    print(n*n)
else:
    list = list[1:]
    print(min(list)*n)
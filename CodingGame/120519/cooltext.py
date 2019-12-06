import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l = input()

a = set()
for i in l: a.add(i)

if len(a)>1:
    for i in range(len(l)):
        print(l[len(l)-i:len(l)]+l[0:len(l)-i])
    print(l)

else:
    print(l)
    print(l)
import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
a = dict()
s = 0
for i in input().split():
    value = int(i)
    if value in a:
        a[value] += 1
    else:
        a[value] = 1
for i in a:
    x = int(a[i] / n * 100)
    if x == i:
        s+=a[i]
print(int(s/n*100))
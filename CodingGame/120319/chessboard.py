import sys
import math


dict = {'p':1, 'n':3, 'b':3, 'r':5, 'q':9}

me=0
him=0

n = int(input())
for i in range(n):
    s = input()
    for j in s:
        if j in 'PNBRQ':
            me+=dict[j.lower()]
        elif j in 'pnbrq':
            him+=dict[j]

print(me-him if me-him!=0 else 'equal')
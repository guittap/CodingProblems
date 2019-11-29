import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
a = []
for i in range(n):
    word = input()
    a.append(word)

a.sort(key=len)
for i in a:
    print(i)
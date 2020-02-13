import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
s = input()
p = input()
sameSpot = 0
inWord = 0

for i in range(n):
    if s[i] == p[i]:
        sameSpot += 1

s = list(s)
for i in p:
    if i in s:
        s.remove(i)
        inWord += 1


print(sameSpot, max(0, inWord-sameSpot))

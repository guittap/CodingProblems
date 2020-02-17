import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

s = input().split()
last = False
truth = True
anser = 0

for i in s:
    last = True if i[0].lower() in "aeiou" else False
    truth = True
    for x in i[1:]:
        if x.lower() in "aeiou" and last:
            truth = False
        elif x.lower() not in "aeiou" and not last:
            truth = False
    if truth:
        anser += 1


print(anser)

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
for i in range(n):
    word = input()[1:]
    a = ""
    for x in word:
        if x == "-":
            a += "0"
        else:
            a += "1"
    print(int(a[0:3], 2), int(a[3:6], 2), int(a[6:9], 2), sep="")

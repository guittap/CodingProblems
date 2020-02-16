import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

s = input()
a = ""

for i in range(len(s)):
    if s[i].isdigit():
        if i == 0:
            a += s[i]

        elif i == len(s)-1:
            a += s[i]

        elif not s[i-1].isdigit() or not s[i+1].isdigit():
            a += s[i]

    last = i


print(a)

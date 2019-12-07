import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

s = input()

if len(s)%2 == 0:
    a = s[0:len(s)//2]
    b = s[len(s)//2:len(s)]
    c = ""

    for i in range(len(a)):
        c += a[i] + b[i]

else:
    a = s[0:len(s)//2+1]
    b = s[len(s)//2+1:len(s)]
    c = ""

    for i in range(len(a)):
        if i == len(b):
            c += a[i]
        else:
            c += a[i] + b[i]
print(c)
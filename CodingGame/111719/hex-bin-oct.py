import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())

a = str(hex(n))
a = a[1::]
b = str(bin(n))
b = b[1::]
c = str(oct(n))
c = c[1::]

print(a+b+c)
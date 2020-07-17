import math
import sys
x_1, y_1 = [int(i) for i in input().split()]
x_2, y_2 = [int(i) for i in input().split()]
print((x_1+x_2)//2 if (x_1+x_2) % 2 == 0 else (x_1+x_2)/2,
      (y_1+y_2)//2 if (y_1+y_2) % 2 == 0 else (y_1+y_2)/2)


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

a = complex(*[int(i) for i in input().split()])
b = complex(*[int(i) for i in input().split()])
c = (a+b)/2

print(f"{c.real:g} {c.imag:g}")

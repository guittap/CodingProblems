import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

x_1, y_1 = [int(i) for i in input().split()]
x_2, y_2 = [int(i) for i in input().split()]

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
a = ((x_1 + x_2) / 2)
b = ((y_1 + y_2) / 2)


if a==0 and b==0:
    print(0,0)
    
elif a==0:
    print(0,b if b/int(b)!=1  else int(b))
    
elif b==0:
    print(a if a/int(a)!=1 else int(a),0)

else:
    print(a if a/int(a)!=1 else int(a), b if b/int(b)!=1  else int(b))
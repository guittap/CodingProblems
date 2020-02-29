import sys
import math

x = int(input())
answer = 1

while (answer * len(str(answer)) <= x):
    answer *= 10

if x//len(str(answer//10)) == 10000000000:
    print(x//len(str(answer//10))-1)
else:
    print(x//len(str(answer//10)) if len(str(answer//10))
          > 1 else x if x < 10 else 9)

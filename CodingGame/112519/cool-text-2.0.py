import sys
import math

s = input()
if len(s)<16:
    print(" "*(16-len(s))+s)
else:
    for i in range(len(s)-16+1):
        print(s[i:i+16])
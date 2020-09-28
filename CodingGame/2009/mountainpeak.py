import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
ans = 0
for i in range(n):
    line = input()
    ans += line.count("/\\")
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(ans)
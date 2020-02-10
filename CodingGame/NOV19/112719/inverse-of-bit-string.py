import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

b = bin(int(input()))[2:]
answer = ""

for i in b:
    if int(i) == 0:
        answer += "1"
    else:
        answer += "0"

print(int(answer, 2))

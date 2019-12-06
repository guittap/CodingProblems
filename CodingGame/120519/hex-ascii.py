import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

value_count = int(input())
for value in input().split():
    a = int(value,16)
    print(chr(a),end="")
import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

s = input()
numbers=0
letters=0

for i in s:
    if i.isdigit():
        numbers+=1
    elif i.isalpha():
        letters+=1

print(round(letters/numbers))
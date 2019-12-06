import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

sentence = input()

for i in sentence:
    if i.lower() in "aeiou":
        print(i+"p"+i,end="")
    else:
        print(i,end="")
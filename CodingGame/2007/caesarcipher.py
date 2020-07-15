import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

text = input()

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

alpha = "abcdefghijklmnopqrstuvwxyz"

for i in range(len(text)):
    if text[i].islower():
        print(alpha[(alpha.index(text[i])+i) % 26], end="")
    elif text[i].isupper():
        u = text[i].lower()
        print(alpha[(alpha.index(u)+i) % 26].upper(), end="")
    else:
        print(text[i], end="")

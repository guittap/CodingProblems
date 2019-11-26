import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

dna = input()

for i in dna:
    if i == "A":
        print("T",end="")
    elif i == "T":
        print("A",end="")
    elif i == "G":
        print("C",end="")
    elif i == "C":
        print("G",end="")
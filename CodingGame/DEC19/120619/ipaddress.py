import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

w = input()

asciisum = sum(ord(i) for i in w)

print(asciisum%256,asciisum%256*2%256,asciisum%256*3%256,asciisum%256*4%256,sep=".")
import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

word = input()
a = ""

for i in range(len(word)//2):
    a+=word[i]+word[len(word)-1-i]

print(a)
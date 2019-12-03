import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

input = input()

iterator=0
final=""
for i in input:
    if i.isalpha():
        final+= i.lower() if iterator%2 else i.upper()
        iterator+=1
    else:
        final+=i

print(final)
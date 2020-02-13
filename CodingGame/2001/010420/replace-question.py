import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

binary = input()  # The input string.
qCount = binary.count("?")
for i in range(2**qCount):
    binRep = str(bin(i))[2:]
    possible = "0"*(qCount-len(binRep))+binRep
    index = 0
    answer = ""
    for x in binary:
        if x=="?":answer+=possible[index];index+=1
        else: answer+=x
    print(answer)
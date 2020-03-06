import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

sentence = input().split()

answer = "...."

if sentence[0:2] == ['Simon', 'says']:
    writeString = sentence[2:]
    if 'write' in writeString:
        answer = ""
        for i in range(writeString.index('write')+1, len(writeString)):
            answer += writeString[i]+" "

print(answer[:-1] if len(answer) > 1 else "...")

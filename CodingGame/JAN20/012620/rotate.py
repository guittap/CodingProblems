import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

sentence = input().split()
temp = list()

for i in range(len(sentence)):
    temp.append(sentence.pop())
    sentence = temp+sentence
    temp.pop()
    truth = True
    for j in range(len(sentence)-1):
        if len(sentence[j])>len(sentence[j+1]):
            truth = False
    if truth:
        print(*sentence)
        exit()

print("ERROR")

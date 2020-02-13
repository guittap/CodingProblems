import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
listOfNums = []
for i in range(n):
    a = int(input())
    listOfNums.append(a)
    
firstIndex = listOfNums[0]
currentIndex = listOfNums[firstIndex]
for i in range(n):
    if currentIndex == 0:
        print("true")
        exit()
    currentIndex = listOfNums[currentIndex]
    
print("false")
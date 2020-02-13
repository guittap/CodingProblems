import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

r, c = [int(i) for i in input().split()]
matrix = []
answer = ""

for i in range(r):
    matrix.append([])
    for j in input().split():
        k = int(j)
        matrix[i].append(k)
        
for i in range(r-2):
    for j in range(c - 2):
        middle = matrix[i+1][j+1]
        if matrix[i+2][j+1] < middle and matrix[i][j+1] < middle and matrix[i+1][j+2] < middle and matrix[i+1][j] < middle:
            answer = middle
            
print(answer if answer != "" else -666)
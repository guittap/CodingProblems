import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.d\\


enemyDict = {}

h, d = [int(i) for i in input().split()]
n = int(input())
for i in range(n):
    eh, ed = [int(j) for j in input().split()]
    enemyDict[i] = [eh, ed]

currEnemy = 0

while h > 0 and currEnemy < n:
    enemyDict[currEnemy][0] -= d
    if enemyDict[currEnemy][0] < 0:
        currEnemy += 1
    for i in range(currEnemy, n):
        h -= enemyDict[i][1]


print("fight" if currEnemy == n else "flee")

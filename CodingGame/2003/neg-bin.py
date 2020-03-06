import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = input()

answer = 0
num = 0
for i in n[::-1]:
    answer += (int(i)*((-2)**num))
    num += 1


print(answer)

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

hair, cheek, eye, nose, mouth, chin = input().split()

print(hair*5)
print(cheek+eye+" "+eye+cheek)
print(cheek+" "+nose+" "+cheek)
print(cheek+" "+mouth+" "+cheek)
print(chin if len(chin) ==5 else (" "*((5-len(chin))//2))+chin)
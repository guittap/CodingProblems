# import sys
# import math

# # Auto-generated code below aims at helping you parse
# # the standard input according to the problem statement.

# x = int(input())
# x = str(bin(x))[2:]
# sum = 0
# for i in x:
#     if i=="1":
#         sum+=1
# print(sum)

x = int(input())
print(sum (1 for i in str(bin(x))[2:] if i=='1'))
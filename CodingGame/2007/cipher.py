import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
message = input()
multiplier = n*len(message)

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

out = ""
for i in message:
    if i in "qwertyuiopasdfghjklzxcvbnm":
        temp = ord(i)-97
        temp = (temp + multiplier) % 26
        out+= chr(temp+97)
    
    else:
        out+= i


print(out)
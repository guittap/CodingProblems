import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

message = input().split()

string = ""
answer = ""
for i in message:
    if chr(int(i))==" ": answer+=string[::-1]+" "; string = ""
    else:string+=chr(int(i))
    
    
print(answer+string[::-1])

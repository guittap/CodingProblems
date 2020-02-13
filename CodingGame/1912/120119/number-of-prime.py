import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def isprime(n) : 

    if (n < 1) : 
        return False
    if (n <= 3) : 
        return True
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
    return True

n = int(input())
for i in range(n):
    a, b = [int(j) for j in input().split()]

    total = 0
    for i in range(a,b+1,1):
        divisors=0
        for j in range(i):
            if i%(j+1)==0 and isprime(j+1):
                divisors+=1
        if divisors>2:
            total+=1
    print(total)
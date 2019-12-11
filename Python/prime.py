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
print(isprime(n))
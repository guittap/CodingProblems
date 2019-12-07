import sys
import math

FibArray = [0,1] 

def fibonacci(n): 
    if n<0: 
        print("Incorrect input") 
    elif n<=len(FibArray): 
        return FibArray[n-1] 
    else: 
        temp_fib = fibonacci(n-1)+fibonacci(n-2) 
        FibArray.append(temp_fib) 
        return temp_fib 

n = int(input())

l=list()
for i in range(1,n+1):
    l.append(fibonacci(i))
    
print(*l)
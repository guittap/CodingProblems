def p(n):
    if(n<=3):return True
    if(n%2==0 or n%3==0) :return False
    i=5
    while(i*i<=n): 
        if (n%i==0 or n%(i + 2) == 0):return False
        i=i+6
    return True
n=int(input())
a=n+1
b=n-1
while not p(a):a+=1
while not p(b):b-=1
c=(a+b)/2
print("WEAK" if n<c else "STRONG" if n>c else "BALANCED")
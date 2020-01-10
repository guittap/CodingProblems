n=int(input())
for i in range(n):print("."*(n-i)+"*"*(i*2+1)+"."*(n-i))
print("."*n+"*"+"."*n)
a,b=map(int,input().split())
n=int(input())
for i in range(n-2):s=a+b;a=b;b=s
print(a if n<2else b if n<3else s)
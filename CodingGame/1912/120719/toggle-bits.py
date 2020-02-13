a,n=map(int,input().split())
for i in range(n):a=a^(1<<int(input()))
print(a)
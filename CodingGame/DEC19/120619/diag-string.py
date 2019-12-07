a=""
n=int(input())
for i in range(n):l=input();a+=l[i]+l[n-1-i]
print(a[0::2],a[1::2])
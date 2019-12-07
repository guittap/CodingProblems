n=int(input())
p,q=[int(i) for i in input().split()]
a,m=0,0
for i in range(n+1):
    for j in range(n+1):
        if (p*i + q*j == n):
            a=i+j
            if a>m:
                m=a
print(m)
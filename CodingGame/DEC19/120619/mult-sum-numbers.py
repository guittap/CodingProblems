a=1
for i in input().split():a*=sum(int(c)for c in i)
print(a)
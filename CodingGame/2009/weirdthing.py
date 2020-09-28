input()
s=list(map(int,input().split()))
e=sum(s)/3

r=0
for i in range(len(s)):
    if sum(s[r:i]) == e:
        for j in s[r:i]:
            print(j,end=" ")
        r=i
        print("|",end=" ")

    if sum(s[r:i]) > e:
        for j in s[r:i-1]:
            print(j,end=" ")
        r=i-1
        print("|",end=" ")

a=""
for i in s[r:]:
    a+=str(i)+" "

print(a[:-1])
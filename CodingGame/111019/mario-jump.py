n,f,h,l=int(input()),-1,0,0
for i in input().split():
    s=int(i)
    if f<s:
        h+=1
    else:
        l+=1
    f=s
print(h-1,l)
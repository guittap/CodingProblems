n=int(input())
d={}
for i in input():
    if i.isalpha():
        i=i.lower()
        if i in d:
            d[i]+=1
        else:
            d[i]=1
for k in sorted(d):
    print(k*d[k])
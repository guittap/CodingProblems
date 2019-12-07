#my code
d={}
for i in input():
    if i in d:d[i]+=1
    else:d[i]=1
for i in sorted(d.keys()):print(i*d[i])

#best code
s=input()
for c in sorted(set(s)):print(c*s.count(c))
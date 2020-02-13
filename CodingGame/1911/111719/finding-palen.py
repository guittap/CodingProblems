s=input()
l=len(s)
a=s[0:l//2]
b=s[l//2+1:]
b=b[::-1]
for i in range(l//2):
    if a.upper()==b.upper():
        break
    else:
        a=a[0:-1]
        b=b[0:-1]
print("Nothing" if s[0]!=s[l-1] else a)
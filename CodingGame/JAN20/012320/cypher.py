a=input()
l=len(a)
b=""
for i in range(l//2):b+=a[i]+a[l-1-i]
print(b+a[l//2]if l%2else b)
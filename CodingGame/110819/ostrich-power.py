g=input()
w=int(input())
if g=="F":
    a=int(w*1.20)
elif g=="M":
    a=int(w/1.20)
else:
    a="UNKNOWN"
print(a)
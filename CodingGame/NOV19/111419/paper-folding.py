t,h,w=input().split()
a=0
b=0
while b < int(h):
    a+=1
    b=float(t)*2**a
print(a)
print(int(w)*2**a)
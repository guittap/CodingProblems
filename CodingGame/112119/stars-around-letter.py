#my way
c=input()
l=int(input())
z="*"*(l//2)
print(z+c+z if l%2==1 else "CAN'T")

#smart way
c=input()
l=int(input())
z="*"*(l//2)
print(z+c+z if l%2else"CAN'T")
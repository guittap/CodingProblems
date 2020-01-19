input()
b=int(input())
for n in(2,5):
 while b%n==0:b/=n
print(("in"if b!=1else"")+"finite")
input()
a = [int(i)for i in input().split()]
b = sum(i for i in a if i % 2 == 0)
c = sum(i for i in a if i % 2)
d = a[len(a)//2]
print(b, "x", c, "+", str(d)+"^2 =", b*c+(d*d))

input()
a = list(map(int, input().split()))
b = sum(i for i in a if i % 2 < 1)
c = sum(i for i in a if i % 2)
d = a[len(a)//2]
print(f"{b} x {c} + {d}^2 = {b*c+d*d}")

x = input
x()
a = list(map(int, x().split()))
b = sum(i for i in a if i % 2 == 0)
c = sum(i for i in a if i % 2)
d = a[len(a)//2]
x(f'{b} x {c} + {d}^2 = {b*c+d**2}')

x = input
x()
a = list(map(int, x().split()))
b = sum(i for i in a if i % 2 < 1)
c = sum(i for i in a if i % 2)
d = a[len(a)//2]
x(f'{b} x {c} + {d}^2 = {b*c+d*d}')

I = input
I()
c = list(map(int, I().split()))
a = []
b = []
[a.append(i) if i % 2 < 1 else b.append(i) for i in c]
a = sum(a)
b = sum(b)
d = c[(len(c)-1)//2]
I(f'{a} x {b} + {d}^2 = {a*b+d**2}')

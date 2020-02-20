x = input
d = [chr(i)for i in range(65, 91)]+[" ", ".", ","]
a, b = map(int, x().split())
x()
for i in x():
    print(d[(d.index(i)*a+b) % 29], end="")

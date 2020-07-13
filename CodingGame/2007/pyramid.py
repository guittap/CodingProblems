a = int(input())
b = input()
c = input()
t = (a+1)//2 if a % 2 else(a+2)//2
d = []
for i in range(t):
    d.append(c*(t-1-i) + b*(i*2+1) + c*(t-1-i))
if a % 2 == 0:
    d = d[::-1]
for i in d:
    print(i)

# my code
s = input().split(".")
t = int(s[1])
q = t//25
t -= q*25
d = t//10
t -= d*10
n = t//5
print(s[0][1:], q, d, n, t-n*5)

# best code
s = input()
t = int(s[-2:])
p = t % 25
q = p % 10
y = q % 5
print(s[1], t//25, p//10, q//5, y)

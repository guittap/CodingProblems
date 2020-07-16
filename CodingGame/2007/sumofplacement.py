c = input()
s = input()

sum = 0

for i in range(len(s)):
    if s[i] == c:
        sum += i

print(sum)

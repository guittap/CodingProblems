n = int(input())
last = -1
total = 1
for i in range(n):
    curr = int(input())
    if last > curr:
        total += 1
    last = curr

print(total)

n = int(input())
line = ""
for i in range(n):
    line += input()

count = 1
last = ""
for i in line:
    if i == last:
        count += 1
    else:
        print(str(count)+last if count > 1 else last, end="")
        count = 1
    last = i

print(str(count)+last if count > 1 else last, end="")

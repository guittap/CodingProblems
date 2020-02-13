s = input().split()
a = len(s)
print(*s[a//2 if a % 2 else a//2-1:a//2+1], sep="")

s=input()
t=input()
for i in range(len(s)):
    if s[i]!=t[i]:print(t[0:i]+s[i:len(t)])
print(t)
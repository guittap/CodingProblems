s = input()
a = 0
while s!=s[::-1]:
   s=s[0:a]+s[len(s)-a-1]+s[a:]
   a+=1
print(a)
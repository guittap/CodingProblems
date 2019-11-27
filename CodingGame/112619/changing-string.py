p=print
s=input()
f=input()
a=0
for i in f:
    if i=='x'or i=='X':p(s[a].lower()if i=='x'else s[a].upper(),end="");a+=1
    else:p(i,end="")
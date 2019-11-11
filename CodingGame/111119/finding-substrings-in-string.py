s,t,a=input(),input(),0
s=s.upper()
t=t.upper()
for i in range(len(t)-len(s)+1):
    if s==t[i:len(s)+i]:
        a+=1
print(a)
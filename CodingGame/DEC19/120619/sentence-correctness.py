k=input()
l=len(k)
for i in range(int(input())):s=input();print("pass"if sum(1for c in range(l)if s[c].lower()==k[c].lower())/l>=.9else"fail")
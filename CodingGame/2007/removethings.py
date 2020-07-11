m=input()
s=input()
a=s
if "t" in m:s="".join(i for i in s if not i.isalpha())
if "u" in m:s="".join(i for i in s if not i.isdigit())
if "y" in m:s="".join(i for i in s if i.isalnum())
if "N" in m:s=a
print(s,sum(ord(i) for i in set(s)),sep="\n")
input()
a=input().split()
print(len(set(i for i in a if a.count(i)>1)))
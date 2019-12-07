ans="true"
n = int(input())
for i in range(n):
    w = input()
    for x in range(len(w)//2):
        if w[x] != w[len(w)-1-x]:
            ans = "false"
            
print(ans)
#my solution
o,m=input().split()
if o=="ROCK" and m=="PAPER":print("SCISSORS",o)
elif o=="ROCK" and m=="SCISSORS" or o=="ROCK" and m=="ROCK":print(o,"PAPER")
elif o=="PAPER" and m=="SCISSORS":print("ROCK",o)
elif o=="PAPER" and m=="ROCK" or o=="PAPER" and m=="PAPER":print(o,"SCISSORS")
elif o=="SCISSORS" and m=="ROCK":print("PAPER",o)
elif o=="SCISSORS" and m=="PAPER" or o=="SCISSORS" and m=="SCISSORS":print(o,"ROCK")
else:print("CHEATER")

#better solution
r,p,s="ROCK PAPER SCISSORS".split()
z={(r,r):(r,p),(p,p):(p,s),(s,s):(s,r),(r,p):(s,r),(s,r):(p,s),(p,s):(r,p),(p,r):(p,s),(r,s):(r,p),(s,p):(s,r)}
print(*z.get(tuple(input().split()),["CHEATER"]))
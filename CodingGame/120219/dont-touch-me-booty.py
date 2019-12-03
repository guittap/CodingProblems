import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

money = input().split()
price = input().split()

newmoney = []
newprice = []
for i in money:
    newmoney.append(int(i[:-1]))

for i in price:
    newprice.append(int(i[:-1]))

currentbalance = newmoney[0]*100*100 + newmoney[1]*100 + newmoney[2]
realprice = newprice[0]*100*100 + newprice[1]*100 + newprice[2]
moneyremaining = currentbalance-realprice

if moneyremaining<0:
    moneyremaining = currentbalance

goldcount = moneyremaining//10000
silvercount = (moneyremaining-goldcount*10000)//100
bronzecount = moneyremaining-goldcount*10000-silvercount*100

print(str(goldcount)+"G",str(silvercount)+"S",str(bronzecount)+"B")
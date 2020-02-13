#my code
# d={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
# m=int(input())
# y=int(input())
# a=False
# if y%4==0:
#     if y%100==0:
#         if y%400==0:a=True
#     else:a=True
# print(29 if m==2 and a else d[m])

#best code
import calendar
m=int(input())
y=int(input())
print(calendar.monthrange(y,m)[1])
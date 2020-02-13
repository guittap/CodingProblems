import math
t=float(input())
t=math.radians(t)
r=float(input())
print(round(r*math.cos(t),1),round(r*math.sin(t),1),sep=", ")
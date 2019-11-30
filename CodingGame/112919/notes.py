a={0:"C",1:"C#",2:"D",3:"D#",4:"E",5:"F",6:"F#",7:"G",8:"G#",9:"A",10:"A#",11:"B"}
m={"major":(4,7),"minor":(3,7),"diminished":(3,6),"augmented":(4,8)}
s,t=input().split()
c=sum(i for i in range(12)if a[i]==s)
b=c+m[t][0]
d=c+m[t][1]
print(s,a[b]if b<12else a[b-12],a[d]if d<12else a[d-12])
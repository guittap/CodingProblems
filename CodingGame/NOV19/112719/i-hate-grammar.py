n = int(input())
for i in range(n):
    q = input().split()
    part1=""
    part2=""
    w=0
    for i in q:
        if w==0:
            if i=='Was':
                part2='were'
            elif i=='Were':
                part2='was'
            elif i=='Am':
                part2='are'
            elif i=='Are':
                part2='am'
                
            else:
                part2=i.lower()
        elif w==1:
            if i=='I':
                part1='you'
            elif i=='you':
                part1='I'
            else:
                part1=i.lower()
            if i=='they' and part2=='am':
                part2 = 'are'
            if i=='we' and part2=='am':
                part2 = 'are'
            if i=='he' and part2=='were':
                part2 = 'was'
            if i=='she' and part2=='were':
                part2 = 'was'
            if i=='it' and part2=='were':
                part2 = 'was'
            if i=='they' and part2=='was':
                part2 = 'were'
            if i=='we' and part2=='was':
                part2 = 'were'
        w+=1
    
    print("Yes,",part1,part2)
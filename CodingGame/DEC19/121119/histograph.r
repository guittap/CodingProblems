gets
d=[0,0,0,0,0,0,0,0,0]
gets.split.each{|c|d[c.to_i-1]+=1}
i=1
d.each{|c|puts i.to_s+":"+"*"*d[i-1];i+=1}
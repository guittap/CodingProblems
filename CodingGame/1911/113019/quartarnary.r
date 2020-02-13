#my code
gets.to_i.to_s(4).split("").each{|c|c=='0'?(print"GA"):c=='1'?(print"BU"):c=='2'?(print"ZO"):(print"MEU")}

#best code
a=["GA","BU","ZO","MEU"]
gets.to_i.to_s(4).split("").each{|c|print(a[c.to_i])}
gets
l=gets.split
a=""
l.each{|x|l.count(x)>l.length/2?a=x:a}
puts a>""?a:"conspiracy"
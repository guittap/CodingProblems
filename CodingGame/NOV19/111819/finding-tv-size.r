d=gets.to_f
l,w=gets.chomp.split(":")
l,w=l.to_f,w.to_f
a=(l**2+w**2)**(1/2)
b=d/a
puts "#{(l*b).round(2)} x #{(w*b).round(2)}"
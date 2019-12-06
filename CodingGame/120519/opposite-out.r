i=0
a=""
gets.to_i.times{i%2<1?(puts gets.chomp):a+=gets.chomp+"\n";i+=1}
puts a
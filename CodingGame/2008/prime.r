require'prime'
b=0
gets.to_i.times{c=gets.to_i;b+=Prime.prime?(c)?c:0}
puts b
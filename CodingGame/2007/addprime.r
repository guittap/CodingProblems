require 'prime'
n=gets.to_i
s=0
n.times{a=gets.to_i;s+=Prime.prime?(a)? a:0}
p s
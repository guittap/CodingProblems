require'prime'
p Prime.prime?(gets.to_i(16).to_s(2).count("1"))?1:0

require'prime'
p gets.to_i(16).digits(2).sum.prime??1:0

require'prime'
p gets.to_i(16).to_s(2).count("1").prime??1:0
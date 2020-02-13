m=gets.split.map &:to_i
gets.to_i.times{m<<m[-2]+m[-1]}
p m[-3]
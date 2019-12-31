d={}
gets.to_i.times{a,b=gets.split;d[a]=b.to_f}
puts *d.sort_by{|a,b| b} 
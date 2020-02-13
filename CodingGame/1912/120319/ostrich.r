g=gets.chop
w=gets.to_i
puts g=='F'?(w*1.2).to_i: g=="M"?(w/1.2).to_i: 'UNKNOWN'
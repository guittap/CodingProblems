b,w,x,y,z=gets.split.collect{|x|x.to_i}
p x+z<y ? b*x+w*(x+z) : y+z<x ? w*y+b*(y+z) : b*x+w*y
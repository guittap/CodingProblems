n=gets.to_i
i=0
n.times{puts("."*(n-i)+"*"*(i*2+1)+"."*(n-i));i+=1}
puts("."*n+"*"+"."*n)
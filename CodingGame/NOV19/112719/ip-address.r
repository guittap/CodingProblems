#my code
gets.to_i.times do
    i=gets.split("/")
    p 2**(32-i[1].to_i)-2
end

#best code
gets.to_i.times{p 2**(32-gets.split('/')[1].to_i)-2}
p "multiply each number in a list"
n = gets.split().map(&:to_i)
p n.inject :*
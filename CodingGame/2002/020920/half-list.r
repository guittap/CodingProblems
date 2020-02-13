s=gets.split
a=s.length()
puts a%2==1?s[a/2]:s[a/2-1]+s[a/2]
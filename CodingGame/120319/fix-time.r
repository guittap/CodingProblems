n = gets.to_i
n.times do
    h,m,s = gets.chomp.split(?:).map &:to_i
    s+=m*60+h*3600
    h=s/3600
    s%=3600
    puts "%02d:%02d:%02d"%[h,s/60,s%60]
end
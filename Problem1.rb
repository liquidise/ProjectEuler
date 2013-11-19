sum = 0
# All integers between 0 and 1000
(0..1000).each do |i|
  if i % 3 == 0 || i % 5 == 0
    sum += i
  end
end


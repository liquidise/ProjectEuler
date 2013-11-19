file = File.open( 'Problem22_Names.txt', 'r' )


names = file.readline.to_s
names = names.split(',')
names = names.map{ |v| v.gsub('"', '') }
names.sort!

letter_score = {}

('A'..'Z').each_with_index do |letter, i|
  letter_score[ letter ] = i + 1
end


score = 0
names.each_with_index do |name, i|
  word_score = 0

  name.each_char do |char|
    word_score += letter_score[ char ]
  end

  score += (i + 1) * word_score
end

puts score
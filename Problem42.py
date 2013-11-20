triangles = []
for i in range( 0, 21 ):
	triangles.append( i * (i + 1) / 2 )

f = open( 'assets/words.txt', 'r' )

content = f.read()
words = content.replace( '"', '' )
words = words.split( ',' )

are = 0
are_not = 0
for word in words:
	word_value = 0
	for letter in word:
		word_value += ord(letter) - 64

	if word_value in triangles:
		are += 1
		print word
	else:
		are_not += 1

print are, are_not
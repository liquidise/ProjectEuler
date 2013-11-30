key = ['g', 'o', 'd' ]
def decode( message ):
	decoded = ""
	char_sum = 0
	for i in range( 0, len(message) ):
		char = message[ i ]
		number = int( char )
		decoded_char = number ^ ord(key[i % 3])
		char_sum += decoded_char
		decoded += chr( decoded_char )

	print decoded, "\n\n", char_sum

f = open( 'assets/cipher1.txt' )
content = f.read()

content = content.strip()
content = content.split(',')

frequency = {}

decode( content )

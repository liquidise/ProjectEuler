f = open( 'assets/triangle.txt')
numbers = f.read()
pyramid = numbers.split( "\n" )
for row in range( 0, len(pyramid) ):
	pyramid[ row ] = pyramid[ row ].split( " " )

pyramid.pop( len(pyramid) - 1 )


pyramid.reverse()

for row in range( 0, len(pyramid) - 1 ):
	for column in range( 0, len(pyramid[row]) - 1 ):
		pyramid[ row + 1 ][ column ] = int(pyramid[ row + 1 ][ column ]) + max( int(pyramid[row][column]), int(pyramid[row][column + 1]) )

print pyramid[ -1 ][ 0 ]

file = open( 'assets/matrix.txt' )

matrix = []
for line in file:
	numbers = line.split(',')
	numbers = [ int( i ) for i in numbers ]
	matrix.append( numbers )

max_index = len( matrix ) - 1
row = max_index
column = max_index

while row >= 0:
	while column >= 0:
		if row < max_index and column < max_index:
			matrix[ row ][ column ] += min( matrix[ row ][ column + 1], matrix[ row + 1 ][ column ] )
		elif row < max_index:
			matrix[ row ][ column ] += matrix[ row + 1 ][ column ]
		elif column < max_index:
			matrix[ row ][ column ] += matrix[ row ][ column + 1 ]

		column -= 1
	row -= 1
	column = max_index

print matrix[ 0 ][ 0 ]
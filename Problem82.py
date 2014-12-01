def checkUp( row, col ):
	up1 = matrix[ row - 1 ][ col ] + matrix[ row - 1 ][ col + 1 ]
	#if row > 1:
	#	up2 = matrix[ row - 1 ][ col ] + matrix[ row - 2 ][ col ] + matrix[ row - 2 ][ col + 1 ]
	#	up1 = min( up1, up2 )
	return up1

def checkDown( row, col ):
	down1 = matrix[ row + 1 ][ col ] + matrix[ row + 1 ][ col + 1 ]
	# if row < 78:
	# 	down2 = matrix[ row + 1 ][ col ] + matrix[ row + 2 ][ col ] + matrix[ row + 2 ][ col + 1 ]
	# 	down1 = min( down1, down2 )
	return down1




file = open( 'assets/matrix.txt' )


matrix = []
for line in file:
	numbers = line.split(',')
	numbers = [ int( i ) for i in numbers ]
	matrix.append( numbers )

matrix = [
	[131, 673, 234, 103, 18],
	[201, 96, 342, 965, 150],
	[630, 803, 746, 422, 111],
	[537, 699, 497, 121, 956],
	[805, 732, 524, 37, 331]
]


column = 0
row = 0
totals = []


for starting_row in range( 0, 5 ):
	column = 0
	row = starting_row
	totals.append( 0 )
	while column < 4:
		totals[ starting_row ] += matrix[ row ][ column ]
		up = 1000000
		if row > 0:
			up = checkUp( row, column )

		down = 1000000
		if row < 4:
			down = checkDown( row, column )
		right = matrix[ row ][ column + 1 ]


		if right <= up and right <= down:
			# Move Right
			column += 1
		elif up < right and up < down:
			# Move Up
			row -= 1
		else:
			# Move Down
			row += 1
	totals[ starting_row ] += matrix[ row ][ column ]


min_total = totals[ 0 ]
for i, total in enumerate(totals):
	min_total = min( min_total, total )
	# print i, total

print "Min: ", min_total

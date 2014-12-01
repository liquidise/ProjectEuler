def count_rectangles( rows, cols ):
	total = 0

	for height in range( 1, cols + 1 ):
		for width in range( 1, rows + 1 ):
			total += (cols - height + 1) * (rows - width + 1)

	return total


max_size = 80
closest = 2000000
for rows in range( 1, max_size ):
	for cols in range( 1, max_size ):
		count = count_rectangles( rows, cols )

		if abs( 2000000 - count ) < closest:
			closest = abs( 2000000 - count )
			print( str(rows) + " x " + str(cols)) + " => " + str( count ),
			print "  Area: " + str( rows * cols )

cache = {}

def num_ways( number, highest_number ):
	if number == 1 or number == 0:
		return 1

	key = str(number) + "_" + str(highest_number)
	if key in cache:
		return cache[ key ]

	ways = 0
	for i in numbers:
		if i > number or i > highest_number:
			continue

		ways += num_ways( number - i, i )

	cache[ key ] = ways
	return ways

numbers = range( 1, 1000 )
numbers.reverse()

for i in range( 1, 1000 ):
	piles = num_ways( i, numbers[0] )
	print i, piles
	if piles % 1000000 == 0:
		print "FOUND", i, piles
		exit()

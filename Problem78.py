cache = {}

def num_ways( number ):
	if number == 0:
		return 1
	elif number < 0:
		return 0

	if number in cache:
		return cache[ number ]

	ways = 0
	i = -1 - number
	while i < number:
		i += 1

		if i == 0:
			continue
		elif i % 2 == 0:
			ways -= num_ways( number - ((i * (3 * i - 1)) / 2) )
		else:
			ways += num_ways( number - ((i * (3 * i - 1)) / 2) )

	cache[ number ] = ways
	return ways

MAX = 1000

numbers = range( 1, MAX + 1 )
numbers.reverse()

for i in range( 1, MAX ):
	piles = num_ways( i, numbers[0] )
	# print i, piles
	if piles % 100 == 0:
		print "FOUND", i, piles

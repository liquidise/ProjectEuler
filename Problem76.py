cache = {}

def num_ways( number, highest_currency ):
	if number == 1 or number == 0:
		return 1

	key = str(number) + "_" + str(highest_currency)
	if key in cache:
		return cache[ key ]

	ways = 1
	for i in currencies[ 0:-1 ]:
		if i > number or i > highest_currency:
			continue

		ways += num_ways( number - i, i )

	cache[ key ] = ways
	return ways

currencies = range( 1, 100 )
currencies.reverse()

print num_ways( 100, 99 )

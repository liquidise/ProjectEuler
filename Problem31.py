def num_ways( number, highest_currency ):
	if number == 1 or number == 0:
		return 1

	ways = 1
	for i in currencies[ 0:-1 ]:
		if i > number or i > highest_currency:
			continue

		ways += num_ways( number - i, i )

	return ways

currencies = [ 1, 2, 5, 10, 20, 50, 100, 200 ]
currencies.reverse()

print num_ways( 200, 200 )

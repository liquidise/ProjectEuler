cache = { 0: 1, 1: 0, 2: 1 }

def num_ways( number, first ):
	global cache
	if number in cache:
		return cache[ number ]

	ways = 1
	for i in currencies[ 100 - number + 1: ]:
		if first:
			print " ", number, "-", i, "=", number - i, "=>",
		ways_for_x = num_ways( number - i, False )
		if first:
			print ways_for_x
		if not (number - i) in cache:
			cache[ number - i ] = ways_for_x
		ways += ways_for_x

	return ways

currencies = []
for i in range( 0, 100 ):
	currencies.append( 100 - i )

# for i in range( 1, 7 ):
# 	print i
# 	num_ways( i, True )


value = 1
for i in range( 1, 101 ):
	value /= 1 - x ** i

print value
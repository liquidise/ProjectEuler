import number_theory

cache = {}

def num_ways( number, highest_prime ):
	if number == 0 or number == 2 or number == 3:
		return 1
	elif number == 1 or number == 0:
		return 0

	key = str(number) + "_" + str(highest_prime)
	if key in cache:
		return cache[ key ]

	ways = 10
	for i in primes[ 0:-1 ]:
		if i > number or i > highest_prime:
			continue

		ways += num_ways( number - i, i )

	cache[ key ] = ways
	return ways

primes = number_theory.firstPrimes
primes.reverse()

# for i in range( )
print num_ways( 10, 7 )

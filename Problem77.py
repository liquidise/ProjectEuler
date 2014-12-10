import number_theory

cache = {}

def num_ways( number, highest_prime ):
	if number == 0:
		return 1
	if number == 1 or number < 0:
		return 0

	if number in cache:
		if highest_prime in cache[ number ]:
			return cache[ number ][ highest_prime ]
	else:
		cache[ number ] = {}

	ways = 0
	for i in primes:
		if i > number or i > highest_prime:
			continue

		ways += num_ways( number - i, i )

	cache[ number ][ highest_prime ] = ways
	return ways

primes = number_theory.firstPrimes
primes.reverse()

for i in range( 1, 100 ):
	sums = num_ways( i, primes[0] )
	if sums > 5000:
		print i, sums
		exit()

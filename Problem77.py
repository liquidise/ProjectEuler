import number_theory

cache = {}

def num_ways( number, highest_prime ):
	if number == 0:
		return 1
	if number == 1 or number < 0:
		return 0

	key = str(number) + "_" + str(highest_prime)
	if key in cache:
		return cache[ key ]

	ways = 0
	for i in primes:
		if i > number or i > highest_prime:
			continue

		ways += num_ways( number - i, i )

	cache[ key ] = ways
	return ways

primes = number_theory.firstPrimes
primes.reverse()

for i in range( 1, 100 ):
	sums = num_ways( i, primes[0] )
	if sums > 5000:
		print i, sums

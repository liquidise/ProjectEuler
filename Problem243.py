from number_theory import *

def set_factor( number ):
	index = 0
	divsior = 2
	factors = set()

	if isPrime( number ):
		return set([ number ])

	while divsior <= number:
		if index >= len( firstPrimes ):
			divsior = getNextPrime( divsior )
			firstPrimes.append( divsior )
		else:
			divsior = firstPrimes [ index ]

		if number % divsior == 0:
			number /= divsior
			factors.add( divsior )
		else:
			index += 1

	return factors


def share_factor( number, factors_to_find ):
	index = 0
	divsior = 2

	while divsior <= number:
		if number % divsior == 0 and divsior in factors_to_find:
			return True
		else:
			index += 1

		if index >= len( firstPrimes ):
			divsior = getNextPrime( divsior )
			firstPrimes.append( divsior )
		else:
			divsior = firstPrimes[ index ]


	return False


result = 15499.0 / 94744

limit = 50000000
denominator = 0
while denominator < limit:
	denominator += 30030

	denom_factors = set_factor( denominator )

	resilient = denominator - 1
	short_circuit = set()
	for numerator in range( 1, denominator ):
		break_out = False
		for num in short_circuit:
			if numerator % num == 0:
				break_out = True
				break

		if break_out:
			continue

		if share_factor( numerator, denom_factors ):
			resilient -= (denominator - numerator) / numerator
			for i in short_circuit:
				factor = numerator * i
				if denominator % factor == 0:
					resilient += (denominator - i) / factor
			short_circuit.add( numerator )

	ratio = float( resilient ) / (denominator - 1)
	if ratio < result:
		print "FOUND", denominator, ratio
	elif ratio < .5:
		print denominator, resilient, denominator - 1, "  ", ratio

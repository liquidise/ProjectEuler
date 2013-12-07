from number_theory import *
from string_utils import is_permutation

first = True
while firstPrimes[ -1 ] < 4000:
	new = getNextPrime( firstPrimes[-1] )
	if first and new > 3162:
		first = False
		start_point = len( firstPrimes )
	firstPrimes.append( new )

minimums = (None, 2)
for i in range( start_point, len(firstPrimes) ):
	for j in range( start_point, start_point - 150, -1 ):
		number = firstPrimes[ i ] * firstPrimes[ j ]

		if number >= 10 ** 7:
			continue

		coprimes = totient( number )
		ratio = float( number ) / coprimes

		if ratio < minimums[1] and is_permutation( str(number), str(coprimes) ):
			minimums = ( number, ratio )
			print number, coprimes, ratio

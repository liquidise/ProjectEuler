import math
from operator import mul

firstPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,
			47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107,
			109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173,
			179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239,
			241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311,
			313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383,
			389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457,
			461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541,
			547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613,
			617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683,
			691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769,
			773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857,
			859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941,
			947, 953, 967, 971, 977, 983, 991, 997]

def isPrime( num ):
	if num < 2:
		return False

	root = int( math.sqrt(num) )

	# Check all primes < 1000
	for i in firstPrimes:
		if i > root:
			return True
		if num % i == 0:
			return False

	# Check remaining odd numbers starting with 1009 (first prime > 1000)
	for i in range( firstPrimes[-1] + 2, root, 2 ):
		if isPrime( i ):
			firstPrimes.append( i )
			if i > root or num % i == 0:
				return False

	return True


def getNextPrime( number ):
	if number % 2 == 0:
		number += 1
	else:
		number += 2

	while not isPrime( number ):
		number += 2

	return number

def isPandigital( number ):
	str_number = str( number )
	digits = [ '1', '2', '3', '4', '5', '6', '7', '8', '9' ]

	if len( str_number ) != 9:
		return False

	for digit in digits:
		if str_number.count( digit ) != 1:
			return False

	return True

def totient( number ):
	factors = exp_factor( number )

	product = 1
	for p, exp in factors:
		product *= (p - 1) * p ** (exp - 1)
	return product

def gcd( a, b ):
	while b > 0:
		a, b = b, a % b
	return a




def share_factors( num1, num2 ):
	return len( set(factor(num1)) & set(factor(num2)) ) > 0

def exp_factor( number ):
	index = 0
	divisor = 2
	factors = {}

	if isPrime( number ):
		return [ (number, 1) ]

	factor_cap = number / 2

	while divisor <= number and divisor <= factor_cap:
		if index >= len( firstPrimes ):
			divisor = getNextPrime( divisor )
			firstPrimes.append( divisor )
		else:
			divisor = firstPrimes [ index ]

		if number % divisor == 0:
			number /= divisor
			if divisor in factors:
				factors[ divisor ] += 1
			else:
				factors[ divisor ] = 1
		else:
			index += 1

	array = []
	for num in factors:
		array.append( (num, factors[num]) )

	return array

factor_cache = {}
def factor( number ):
	global factor_cache

	original_number = number
	index = 0
	divisor = 2
	factors = []

	if original_number in factor_cache:
		return factor_cache[ original_number ]

	if isPrime( number ):
		factor_cache[ number ] = [ number ]
		return [ number ]

	while divisor <= number:
		if index >= len( firstPrimes ):
			divisor = getNextPrime( divisor )
			firstPrimes.append( divisor )
		else:
			divisor = firstPrimes [ index ]

		if number % divisor == 0:
			number /= divisor
			factors.append( divisor )
		else:
			index += 1

	factor_cache[ original_number ] = factors
	return factors

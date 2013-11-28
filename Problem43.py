primes = [ 17, 13, 11, 7, 5, 3, 2 ]

all_digits = set([ '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' ])

multiples = {}
for prime in primes:
	multiples[ prime ] = []
	multiplier = 1 # 17 * 6 is the lowest to get a 3 digit product
	product = 1
	while int(product) < 1000:
		product = multiplier * prime
		product = "%03d" % product

		list_product = list( product )
		set_product = set( list_product )

		if len( set_product ) == 3 and len( list_product ) == 3:
			multiples[ prime ].append( list_product )

		multiplier += 1

def numWays( index, existing_digits, second_digit, third_digit ):
	if index > 6 and existing_digits.count('0') > 0:
		number = "".join( existing_digits )
		all_ways.add( number )
		return 1
	elif index > 6:
		return 0

	ways = 0
	for number in multiples[ primes[index] ]:
		if existing_digits.count(number[0]) == 0 and number[1] == second_digit and number[2] == third_digit:
			digits = [number[0]] + existing_digits
			spaces = ""
			ways += numWays( index + 1, digits, number[0], number[1] )

	return ways


ways = 0
all_ways = set()
for k in multiples[17]:
	ways += numWays( 1, k, k[0], k[1] )

all_ways = list( all_ways )
all_ways.sort()

all_sum = 0
for num in all_ways:
	if num[0] == '1':
		num = '4' + num
	else:
		num = '1' + num
	all_sum += int( num )

print all_sum

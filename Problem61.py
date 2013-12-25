def check_tree( options, found, initial ):
	global totals

	if len(found) == 6:
		return True

	for num, method in options:
		if method in found or not (num % 100) in first_digits:
			continue

		if len(found) == 0:
			initial = num / 100
		elif len(found) == 5 and num % 100 != initial:
			continue

		if check_tree( first_digits[num % 100], found | set([method]), initial ):
			print num,
			totals += num
			return True

	return False

def add_new( number, method ):
	if number >= 1000 and number <= 9990:
		if not number / 100 in first_digits:
			first_digits[ number / 100 ] = []

		first_digits[ number / 100 ].append( (number, method) )

first_digits = {}
totals = 0

for i in range( 5, 200 ):
	add_new( i * ( i + 1 ) / 2, 3 )
	add_new( i ** 2, 4 )
	add_new( i * ( (3 * i) - 1 ) / 2, 5 )
	add_new( i * ( (2 * i) - 1 ), 6 )
	add_new( i * ( (5 * i) - 3 ) / 2, 7 )
	add_new( i * ( (3 * i) - 2 ), 8 )

for k in first_digits:
	if check_tree( first_digits[k], set(), None ):
		break

print "\n\n", totals

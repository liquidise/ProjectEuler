factorials = {
	'0': 1,
	'1': 1,
	'2': 2,
	'3': 6,
	'4': 24,
	'5': 120,
	'6': 720,
	'7': 5040,
	'8': 40320,
	'9': 362880
}

total = 0
for i in range( 2, 100000 ):
	digit_sum = 0
	for char in str( i ):
		digit_sum += factorials[ char ]
		if digit_sum > i:
			break

	if digit_sum == i:
		total += i

print total

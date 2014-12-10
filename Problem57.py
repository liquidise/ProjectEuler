prev_denominator = 1
denominator = 2

count = 0
for i in range( 1, 1000 ):
	temp = denominator
	denominator = (2 * denominator) + prev_denominator
	prev_denominator = temp

	if int( str(denominator)[0:3] ) >= 707:
		count += 1

print count

total = 0
for base in range( 10, 10000 ):
	number = base
	lychrel = True
	for i in range( 1, 50 ):
		number = number + int( str(number)[::-1] )
		str_number = str( number )

		if str_number == str_number[::-1]:
			lychrel = False
			break
	if lychrel:
		total += 1

print total

for number in range( 125874, 1000000 ):
	set_num = set( list(str(number)) )
	found = True
	for i in [6, 5, 4, 3, 2]:
		test = set( list(str(number * i)) )

		if len(set_num ^ test ) > 0:
			found = False
			break

	if found:
		print number
		exit()

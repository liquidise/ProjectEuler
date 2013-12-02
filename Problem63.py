count = 0
for exp in range( 1, 100 ):
	for base in range( 1, 100 ):
		if len( str(base ** exp) ) == exp:
			count += 1

print count

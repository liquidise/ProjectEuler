from number_theory import isPandigital

finds = []
for i in range( 2, 9999 ):
	found = True
	digits = list( str(i) )
	set_digits = set( digits )

	for multiplier in range( 2, 10 ):
		new_product = i * multiplier
		new_product = list( str(new_product) )
		digits += new_product
		set_digits = set_digits | set( new_product )

		if '0' in set_digits or len( set_digits ) != len( digits ):
			found = False
			break
		elif len( digits ) == 9:
			found = True
			break

	if found:
		finds.append( "".join( digits ) )

finds.sort()

print finds[ -1 ]

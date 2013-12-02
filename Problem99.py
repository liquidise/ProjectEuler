from number_theory import factor

f = open( 'assets/base_exp.txt' )


for line in f:
	numbers = line.split( ',' )
	base = int( numbers[ 0 ] )
	exp = int( numbers[ 1 ] )

	print exp, factor( exp )


import itertools, number_theory, string

for i in range( 3, 9 ):
	permute = ""
	for k in range( 1, i ):
		permute += str( k )
	
	numbers = itertools.permutations( permute )
	
	for k in numbers:
		number = int( string.join( k, "") )
		if number_theory.isPrime( number ):
			print number
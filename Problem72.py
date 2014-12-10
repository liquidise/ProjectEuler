from number_theory import totient

count = 0
for i in range( 1, (10 ** 6) + 1 ):
	if i % 1000 == 0:
		print i
	count += totient( i )

print count







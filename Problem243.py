from number_theory import totient

result = 15499.0 / 94744

denominator = 0
while denominator < 10000000000:
	denominator += 510510

	co_prime = totient( denominator )

	ratio = float( co_prime ) / (denominator - 1)
	if ratio < result:
		print denominator, "  ", ratio
		exit()

from number_theory import firstPrimes

product = 1
for i in firstPrimes:
	product *= i
	if product > 1000000:
		print product / i
		exit()

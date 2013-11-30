from number_theory import isPrime

i = 1
primes = 0
checked = 1
prev_value = 1
while i < 4 or primes / float(checked) > .1:
	if i % 1000 == 0:
		print i, primes / float(checked)

	corners = [
		prev_value + (2 * i),
		prev_value + (4 * i),
		prev_value + (6 * i)
	]

	# print i, corners
	prev_value += 8 * i

	for j in corners:
		if isPrime( j ):
			primes += 1

	checked += 4
	i += 1

print checked, primes

print (i - 1) * 2 + 1, primes / float(checked)

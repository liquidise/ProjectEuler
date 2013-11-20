def isAbundant( num ):
	factors = [1]
	for i in range( 2, int(num / 2) ):
		if num % i == 0:
			# if num % i == 0 and i != num / i:
			factors += [ i ]
			factors += [ num / i ]

	sum = 0
	for i in set(factors):
		sum += i
	return sum > num

abundantNums = {}
print "Finding abundant numbers..."
for i in range(12, 28123):
# for i in range(12, 270):
	if isAbundant( i ):
		abundantNums[ i ] = True
print "Found", len(abundantNums), "abundant numbers"

sum = 0
print "\nCalculating adundant sums..."
for num in range( 1, 28123 ):
	keys = list( (k for k in abundantNums.keys() if k < num and k >= num / 2) )
	keys.reverse()

	if num % 1000 == 0:
		print "Checking", num

	found = True
	for k in keys:
		found = True
		diff = num - k
		if diff in abundantNums:
			found = False
			break
	if found:
		sum += num

print "Sum =", sum

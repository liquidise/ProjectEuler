end_at_89 = {}
end_at_1 = {}

total = 0
for num in xrange( 2, 10000000):
	if num % 100000 == 0:
		print num
	current_step = num
	numbers_hit = set()
	while current_step not in end_at_1 and current_step not in end_at_89 and current_step != 1 and current_step != 89:
		product = 0
		for digit in str( current_step ):
			product += int( digit ) ** 2
		numbers_hit.add( product )
		current_step = product

	if current_step in end_at_89:
		total += 1
	elif current_step == 89:
		total += 1
		for i in numbers_hit:
			end_at_89[ i ] = True
	elif current_step == 1:
		for i in numbers_hit:
			end_at_1[ i ] = True

print total
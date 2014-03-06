values = [2, 3]

for i in range( 2, 100 ):
	sequence = 1
	if i % 3 == 2:
		sequence = 2 + 2 * (i / 3)

	next_value = values[i - 2] + values[i - 1] + (values[i - 1] * (sequence - 1))
	values.append( next_value )

total = 0
for char in str(values[-1]):
	total += int( char )
print total

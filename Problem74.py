from math import factorial

cache = {}
for i in range( 0, 10 ):
	cache[ str(i) ] = factorial( i )

i = 1
count = 0
while i < 1000000:
	prev_number = i
	numbers = set()
	while not prev_number in numbers:
		numbers.add( prev_number )
		new_number = 0
		for digit in str(prev_number):
			new_number += cache[ digit ]
		prev_number = new_number

	if len( numbers ) == 60:
		 print i
		 count += 1
	i += 1

print "\n\n" + str(count)

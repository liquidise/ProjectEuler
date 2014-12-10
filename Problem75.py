from math import sqrt

count = 0

ratios = set()
for number in range( 6, 1000 ):
	lower_bound = number / 6
	middle = number / 3

	total_for_num = 0
	for a in range( middle, lower_bound, -1 ):
		for b in range( middle, 2 * middle - a ):
			sides = (a ** 2) + (b ** 2)
			if sides == (number - a - b) ** 2:
				total_for_num += 1
				ratios.add( a / float(b) )
				print number, ";", a, b

	if total_for_num == 1:
		count += 1

print count, ratios
from itertools import permutations, combinations

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
first_five = combinations( numbers, 5 )

for combo in first_five:
	this_combo = list( combo )
	orderings = permutations( this_combo )
	for order in orderings:
		inner_sums = []
		highest_sum = 0
		highest_sum_numbers = []
		for i in range( 0, 5 ):
			upper_index = (i + 1) % 5
			this_sum = order[ i ] + order[ upper_index ]
			if this_sum > highest_sum:
				highest_sum = this_sum
				highest_sum_numbers = [ order[i], order[upper_index] ]

			inner_sums.append( this_sum )
		if len( set(inner_sums) ) == 5:
			inner_sums.sort()
			remaining = list( set(numbers) - set(order) )
			remaining.append( 10 )
			remaining.sort()

			total_sums = set()
			for i in range( 0, 5 ):
				total_sums.add( inner_sums[i] + remaining[4 - i] )

			if len( total_sums ) == 1:
				ordered_list = list( order )
				ordered_list.sort()

				print order, remaining, str(remaining[0]) + str(highest_sum_numbers[0]) + str(highest_sum_numbers[1])

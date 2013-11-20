import number_theory

four_in_a_row = 0
i = 0
while four_in_a_row < 4:
	i += 1

	factors = number_theory.factor( i )

	if len( set(factors) ) >= 4:
		print i, factors
		four_in_a_row += 1
	elif four_in_a_row > 0:
		print
		four_in_a_row = 0

from number_theory import share_factors

max_ratio = 3.0 / 7

closest = ( None, 100 )
for denom in range( 10 ** 6, 999900, -1 ):
	numerator = int( denom * max_ratio )

	distance_from_three_sevenths = max_ratio - (float(numerator) / denom)

	if distance_from_three_sevenths < closest[ 1 ] and not share_factors( numerator, denom ):
		closest = ( numerator, distance_from_three_sevenths )
		print denom, closest

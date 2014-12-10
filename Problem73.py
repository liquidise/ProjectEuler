from number_theory import *
from datetime import datetime

min_ratio = 1.0 / 3
max_ratio = .5

count = 0
for denom in range( 2, 12001 ):
	for numerator in range( int(min_ratio * denom), int(max_ratio * denom) + 1 ):
		if gcd( numerator, denom ) > 1:
			continue

		ratio = float(numerator) / denom

		if ratio > min_ratio and ratio < max_ratio:
			count += 1

print count

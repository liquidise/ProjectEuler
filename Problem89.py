def numeric_value( numerals ):
	value = 0
	i = 0
	while i < len(numerals):
		numeral = numerals[ i ]
		if i + 1 < len(numerals) and numeral_value[ numeral ] < numeral_value[ numerals[ i + 1 ] ]:
			value += numeral_value[ numerals[ i + 1 ] ] - numeral_value[ numeral ]
			i += 2
		else:
			value += numeral_value[ numeral ]
			i += 1
	return value

def build_number( number ):
	to_roman = ''
	digits = list( str( number ) )

	for j, digit in enumerate(digits):
		digit = int( digit )
		place = 10 ** ( len(digits) - j - 1)

		temp = digit * place

		while temp > 0:
			i = 0
			while i < len( values ):
				if temp < values[ i ]:
					i += 1
				else:
					for index, short_cut in enumerate(short_cuts):
						if temp == short_cut:
							to_roman += short_cut_numerals[ index ]
							temp -= short_cut
					if temp > 0:
						temp -= values[ i ]
						to_roman += numerals[ i ]
	return to_roman

numeral_value = { 'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1 }
values = [ 1, 5, 10, 50, 100, 500, 1000 ]
numerals = [ 'I', 'V', 'X', 'L', 'C', 'D', 'M' ]
short_cuts = [4, 9, 40, 90, 400, 900]
short_cut_numerals = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']
values.reverse()
numerals.reverse()

f = open( 'assets/roman.txt' )

total = 0

for line in f:
	these_numerals = list( line.strip() )
	number = numeric_value( these_numerals )
	new_numerals = build_number( number )

	if len(these_numerals) > len(new_numerals):
		total += len(these_numerals) - len(new_numerals)
		print number, new_numerals

print "\n\n", total
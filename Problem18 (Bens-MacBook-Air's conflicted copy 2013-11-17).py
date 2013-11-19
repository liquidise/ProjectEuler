pyramid = [
    [75],
    [95,  64],
    [17,  47,  82],
    [18,  35,  87,  10],
    [20,  04,  82,  47,  65],
    [19,  01,  23,  75,  03,  34],
    [88,  02,  77,  73,  07,  63,  67],
    [99,  65,  04,  28,  06,  16,  70,  92],
    [41,  41,  26,  56,  83,  40,  80,  70,  33],
    [41,  48,  72,  33,  47,  32,  37,  16,  94,  29],
    [53,  71,  44,  65,  25,  43,  91,  52,  97,  51,  14],
    [70,  11,  33,  28,  77,  73,  17,  78,  39,  68,  17,  57],
    [91,  71,  52,  38,  17,  14,  91,  43,  58,  50,  27,  29,  48],
    [63,  66,  04,  68,  89,  53,  67,  30,  73,  16,  69,  87,  40,  31],
    [04,  62,  98,  27,  23,   9,  70,  98,  73,  93,  38,  53,  60,  04,  23]
]


row_max = 0
values = []
for row in range( 0, len(pyramid) ):
	print "", row_max, values
	row_max = 0
	values = []
	for column in range( 0, len(pyramid[row]) ):
		if row >= len(pyramid) - 1:
			continue

		value = pyramid[ row ][ column ]
		value2 = pyramid[ row + 1 ][ column ]

		if row_max < value + value2:
			values = [ value, value2 ]
			row_max = value + value2

		value2 = pyramid[ row + 1 ][ column + 1 ]

		if row_max < value + value2:
			values = [ value, value2 ]
			row_max = value + value2



exit()


pyramid.reverse()

column = 0

for column in range( 0, len(pyramid) ):
	total_sum = 0
	for row in range( 0, len(pyramid) ):
		total_sum += pyramid[ row ][ column ]

		if row < len(pyramid) and column > 0:
			if column >= len( pyramid[row + 1] ):
				column -= 1
			elif pyramid[ row + 1 ][ column - 1] > pyramid[ row + 1 ][ column ]:
				column -= 1

	print total_sum

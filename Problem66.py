from math import sqrt

low_squares = set()
squares = {}
for i in range( 1, 1000 ):
	low_squares.add( i ** 2 )



d = 61

values = (8, 1, 8 ** 2 - d * 1 ** 2)
while values[ 2 ] != 1:
	a, b, k = values

	print a, b, k

	m = 6
	found = False
	while not found:
		m += 1
		if (a + m) % k == 0 and abs(m ** 2 - d) % k == 0:
			found = True
	print "m =", m

	print ((a * m) + d) / k, (a + m) / k, (m ** 2 - d) / k
	values = ( ((a * m) + d) / k, (a + m) / k, (m ** 2 - d) / k )

print values



exit()

















max_x = 1
the_d = 0
for d in range( 61, 62 ):
	if d in low_squares:
		continue

	x = 33000000
	found = False
	while not found:
		print x
		x += 1
		x_squared = long(x) ** 2

		if x_squared % d != 1:
			continue

		y = sqrt( ( x_squared - 1.0) / d )

		if y > 0 and y == int(y):
			if x > max_x:
				max_x = x
				the_d = d

			print d, ':', x, y
			found = True

print "d =", the_d, "  x =", max_x

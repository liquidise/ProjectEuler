from math import factorial

def choose( x, y ):
	return factorial(x) / (factorial(y) * factorial(x - y))

total = 0
for i in range( 23, 101 ):
	for j in range( 1, i ):
		if choose( i, j ) > 1000000:
			total += 1

print total

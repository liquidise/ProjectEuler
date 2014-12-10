def sign( point1, point2 ):
	return (0 - point2['x']) * (point1['y'] - point2['y']) - (point1['x'] - point2['x']) * (0 - point2['y']);

def originInTriange( point1, point2, point3 ):
	sign1 = sign( point1, point2 ) < 0
	sign2 = sign( point2, point3 ) < 0
	sign3 = sign( point3, point1 ) < 0

	return sign1 == sign2 and sign2 == sign3

file = open( 'assets/triangle.txt' )

point1 = { 'x': -340, 'y': 495 }
point2 = { 'x': -153, 'y': -910 }
point3 = { 'x': 835, 'y': -947 }

print originInTriange( point1, point2, point3 )

#for line in file:
#	print line

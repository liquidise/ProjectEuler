def sign( point1, point2 ):
	return (0 - point2['x']) * (point1['y'] - point2['y']) - (point1['x'] - point2['x']) * (0 - point2['y']);

def originInTriange( point1, point2, point3 ):
	sign1 = sign( point1, point2 ) < 0
	sign2 = sign( point2, point3 ) < 0
	sign3 = sign( point3, point1 ) < 0

	return sign1 == sign2 and sign2 == sign3

file = open( 'assets/p102_triangles.txt' )

contians = 0
for line in file:
	nums = line.split( "," )
	p1 = {'x': int(nums[0]), 'y': int(nums[1]) }
	p2 = {'x': int(nums[2]), 'y': int(nums[3]) }
	p3 = {'x': int(nums[4]), 'y': int(nums[5]) }

	if originInTriange( p1, p2, p3 ):
		contians += 1

print contians
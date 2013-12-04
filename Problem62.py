cubes = {}
for i in range( 1, 10000 ):
	cube = str(i ** 3)
	if len( cube ) == 12:
		cubes[ cube ] = set( list(cube) )


for cube in sorted(cubes.iterkeys()):
	matches = [ cube ]
	for possible_match in cubes:
		if possible_match == cube or cubes[ possible_match ] != cubes[ cube ]:
			continue

		match = True
		for char in cube:
			if cube.count( char ) != possible_match.count( char ):
				match = False
				break
		if match:
			matches.append( possible_match )

	if len(matches) >= 5:
		print matches
		exit()

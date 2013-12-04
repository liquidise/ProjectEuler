def isIncreasing( number ):
	number = str( number )

	for i in range( 0, len(number) ):
		if i > 0 and int(number[-i - 1]) > int(number[-i]):
			return False
	return True

def isDecreasing( number ):
	number = str( number )

	for i in range( 0, len(number) ):
		if i < len(number) - 1 and int(number[i + 1]) > int(number[i]):
			return False
	return True


def isBouncy( number ):
	return not isIncreasing( number ) and not isDecreasing( number )

bouncy = 0
checked = 0
i = 1
while bouncy == 0 or float(bouncy) / checked < .99:
	if isBouncy( i ):
		bouncy += 1
	checked += 1
	i += 1

print checked
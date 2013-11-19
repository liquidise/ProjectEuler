from number_theory import isPrime
import itertools, math, string

def hasDupes( diffList ):
	seen = []
	for i in diffList:
		seen += [ i ]
		if seen.count( i ) == 2:
			return i
	return False

checked = []
primeSets = []
for i in range( 1009, 9999 ):
	if i in checked or not isPrime( i ):
		continue

	permutes = itertools.permutations( str(i) )

	primes = [ i ]
	for k in set( permutes ):
		number = int( string.join(k, "") )

		if number >= 1000 and isPrime( number ):
			primes += [ number ]
			checked += [ number ]

	primes = set( primes )
	primes = list( primes )
	primes.sort()

	if len( primes ) >= 3:
		primeSets += [ primes ]

diffs = []
for a in primeSets:
	
	diffs = []
	for i, b in enumerate( a ):
		index = i + 1
		while index < len(a):
			difference = b - a[index]
			diffs += [ difference ]
			index += 1

	dupe = hasDupes( diffs )
	if dupe and math.fabs(dupe) == 3330:
		print dupe, "\t", a

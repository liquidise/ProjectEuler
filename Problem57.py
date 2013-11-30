import sys

sys.setrecursionlimit( 1200 )

def next_frac( iteration ):
	if iteration == 0:
		return .5
	else:
		return 1 / (2 + next_frac( iteration - 1 ) )

for i in range( 1, 1000 ):
	print 1 + next_frac( i )



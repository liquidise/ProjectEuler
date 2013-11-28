import math

sums = {}
most = (0, 0)
for i in range(1, 1000):
	for k in range(1, i):
		root = math.sqrt( (i * i) + (k * k) )
		intRoot = int( root )
		if root == intRoot:
			total = i + k + intRoot

			if total > 1000:
				continue

			if total in sums:
				sums[ total ] += 1
			else:
				sums[ total ] = 1

			if most[0] < sums[ total ]:
				most = ( sums[total], total )

print most

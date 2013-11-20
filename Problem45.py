triangles = {}
pents = {}
hexes = {}
for i in range( 1, 100000 ):
	triangles[ (i * (i + 1) / 2) ] = True
	pents[ (i * (3 * i - 1) / 2) ] = True
	hexes[ (i * (2 * i - 1)) ] = True

for key in triangles:
	try:
		if pents[ key ] and hexes[ key ]:
			print key
	except Exception as e:
		pass

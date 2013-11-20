from bigfloat import *

setcontext( Context(precision=10000) )

largest = 0
for i in range( 2, 1000 ):
	value = str( BigFloat( 1.0 ) / BigFloat( i ) )
	value = value[ 2:-1 ]

	for offset in range( 6, 50 ):
		substr = value[ 0:offset ]
		repeat_index = value[ offset:-1 ].find( substr )
		if repeat_index > -1:
			if repeat_index > largest:
				largest = repeat_index
				print '*', i, substr, repeat_index
			else:
				print i, substr, repeat_index
			break

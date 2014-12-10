import re

MIN = 1020304050607080900
MAX = 1929394959697989990

regex = re.compile( "1\d2\d3\d4\d5\d6\d7\d8\d9\d0" )

count = 0
for i in xrange( 1009950500, 1409019170, 10 ):
	sqrt = i * i
	stringRoot = str(sqrt)

	if sqrt > MIN and sqrt <= MAX:
		if regex.match( stringRoot ):
			print i, sqrt
			exit()
		count += 1
	elif sqrt > MAX:
		exit()

import itertools, string

permutes = itertools.permutations( "0123456789" );
bigList = []

for i in permutes:
    num = int( string.join( i, "" ) )
    bigList += [ num ]

print bigList[999999]
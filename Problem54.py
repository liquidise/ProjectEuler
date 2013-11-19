import urllib2

class PokerHand:
	cards = []
	def __init__( self, handString ):
		tempCards = handString.split( " " )
		tempCards.sort()
		
		for i in tempCards:
			card = { "value": i[0], "suit": i[1] }
			self.cards += [ card ]
		print self.cards
	

file = urllib2.urlopen( "http://projecteuler.net/project/poker.txt" )

for line in file:
	line = line.strip()
	hand1 = line[0:14]
	hand2 = line[15:]
	hand = PokerHand( hand1 )
	hand = PokerHand( hand2 )
	exit()
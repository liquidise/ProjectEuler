class PokerHand:
	card_value = { 'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10 }

	def __init__( self, handString ):
		self.cards = []
		self.values = []
		self.suits = []

		tempCards = handString.split( " " )
		tempCards.sort()

		for i in tempCards:
			value = i[ 0 ]
			if value == 'A' or value == 'K' or value == 'Q' or value == 'J' or value == 'T':
				value = self.card_value[ i[0] ]

			card = { "value": int(value), "suit": i[1] }
			self.values.append( card['value'] )
			self.suits.append( card['suit'] )
			self.cards += [ card ]

		self.values.sort()

	def __str__( self ):
		to_string = ''
		for card in self.cards:
			to_string += str(card['value']) + card['suit'] + " "
		return to_string

	def score( self ):
		score = 0
		if self.isFullHouse():
			score = 11
		elif self.isFlush():
			score = 10
		elif self.isStraight():
			score = 9
		elif self.isThreeOfAKind():
			score = 8
		elif self.isTwoPair():
			score = 7
		elif self.isPair():
			score = 6
			s = set()
			for i in self.values:
				if i in s:
					score += (i / 3.0) / 10
				else:
					s.add( i )
		else:
			score = self.values[ 4 ] / 3.0


		return score

	def isFullHouse( self ):
		return len( set(self.values) ) == 2

	def isStraight( self ):
		return len(set(self.values)) == 5 and self.values[0] + 4 == self.values[4]

	def isFlush( self ):
		return len( set(self.suits) ) == 1

	def isThreeOfAKind( self ):
		if len( set(self.values) ) != 3:
			return False

		first_card_appears = self.values.count( self.values[0] )
		second_card_appears = self.values.count( self.values[1] )
		third_card_appears = self.values.count( self.values[2] )

		return first_card_appears == 3 or second_card_appears == 3 or third_card_appears == 3

	def isTwoPair( self ):
		if len( set(self.values) ) != 3:
			return False

		first_card_appears = self.values.count( self.values[0] )
		second_card_appears = self.values.count( self.values[1] )

		return first_card_appears == 2 or second_card_appears == 2

	def isPair( self ):
		return len( set(self.values) ) == 4
		if len( set(self.values) ) != 4:
			return False

		first_card_appears = self.values.count( self.values[0] )
		second_card_appears = self.values.count( self.values[1] )

		return first_card_appears == 2 or second_card_appears == 2



file = open( 'assets/poker.txt' )

tie = 0
player1 = 0
player2 = 0
for line in file:
	line = line.strip()
	hand1 = PokerHand( line[0:14] )
	hand2 = PokerHand( line[15:] )

	score1 = hand1.score()
	score2 = hand2.score()

	if score1 > score2:
		player1 += 1
	elif score2 > score1:
		player2 += 1
	else:
		print score1, "  ", hand1, hand2
		tie += 1

print player1, player2, tie

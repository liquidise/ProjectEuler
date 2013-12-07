def is_permutation( str1, str2 ):
	if len( str1 ) != len( str2 ):
		return False

	for char in str1:
		if str1.count( char ) != str2.count( char ):
			return False

	return True
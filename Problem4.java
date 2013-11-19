public class Problem4 {
	
	static boolean isPalindrome( int num ) {
		String number = "" + num;
		boolean retval = true;
		int forLimit;
		char char1;
		char char2;
		
		if( number.length() % 2 == 0 ) {
			// Find even palindromes
			forLimit = number.length() / 2;
		} else {
			// Find odd palindromes
			forLimit = (number.length() - 1) / 2;
		}
		
		// Check palindrome
		for( int i = 0; i < forLimit && retval; i++ ) {
			char1 = number.charAt(i);
			char2 = number.charAt( number.length() - i - 1 );
			
			retval = (char1 == char2);
		}
		
		return retval;
	}
	
	public static void main( String[] args ) {
		int solution = 0;
		int product;
		
		for( int i = 999; i > 900; i-- ) {
			for( int j = 999; j > 900; j-- ) {
				product = i * j;
				
				if( product > solution && isPalindrome(product) ) {
					System.out.println( "New larger found: " + product );
					solution = product;
				}
			}
		}
		
		System.out.println( "Largest palindrome is: " + solution );
	}
}
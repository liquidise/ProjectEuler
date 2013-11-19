public class Problem17 {
	static int[] NUMS = {0, 3, 3, 5, 4, 4, 3, 5, 5, 4};
	static int[] TEENS = {0, 6, 6, 8, 8, 7, 7, 9, 8, 8};
	static int[] TENS = {0, 3, 6, 6, 5, 5, 5, 7, 6, 6};
	static int HUNDRED = 10; 	// "Hundred and"

	
	static int getNumChars( int num ) {
		int retval = 0;
		
		// Hundreds digit
		if( num >= 100 ) {
			retval += NUMS[ (int)Math.floor(num/100) ];
			retval += HUNDRED;
			
			// Remove "and" from hundred
			if( num % 100 == 0 ) {
				retval -= 3;
			}
		}
		
		// Teens
		if( num%100 > 10 && num%100 < 20 ) {
			retval += TEENS[ num%10 ];
		} else {
			// Tens digit
			retval += TENS[ (int)Math.floor((num%100)/10) ];
			// Ones digit
			retval += NUMS[ num%10 ];
		}
		
		return retval;
	}

	public static void main( String[] args ) {
		int numChars = 0;
		
		for( int i = 1; i < 1000; i++ ) {
			numChars += getNumChars( i );
		}
		
		// Include "one thousand"
		numChars += 11;
		
		System.out.println( "" + numChars );
	}
}
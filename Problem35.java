public class Problem35 {
	private static boolean canBeCircular( long num ) {
		String number = "" + num;
		boolean isPossible = true;
		
		// Ensure none of the digits are 0, 2, 4, 5, 6, 8
		// All of which would cause a non-prime in the permutations
		for( int i = 0; i < number.length() && isPossible; i++ ) {
			isPossible = number.charAt(i) != '0' && number.charAt(i) != '2' &&
							number.charAt(i) != '4' && number.charAt(i) != '5' &&
							number.charAt(i) != '6' && number.charAt(i) != '8';
		}
		
		return isPossible;
	}
	
	private static boolean isCircularPrime( long number ) {
		String num = "" + number;
		char tempChar;
		boolean isPrime;
		
		isPrime = TestPrime.isPrime( Long.parseLong(num) );
		
		for( int i = 0; (i < num.length() - 1) && isPrime; i++ ) {
			tempChar = num.charAt(0);
			num = num.substring( 1 );
			num += tempChar;
			
			isPrime = TestPrime.isPrime( Long.parseLong(num) );
		}
		
		return isPrime;
	}
	
	public static void main( String[] args ) {
		int numCircular = 4; // Auto-include 2, 3, 5, 7
		
		for( long i = 11; i < 1000000; i += 2 ) {
			if( canBeCircular(i) && isCircularPrime(i) ) {
				System.out.println( "#" + (numCircular + 1) + " = " + i );
				numCircular++;
			}
		}
		
		System.out.println( "Total = " + numCircular );
	}
}
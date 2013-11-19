public class Problem46 {	
	public static boolean isGoldbach( int num ) {
		boolean retval = false;
		long prime = 2;
		
		// Must be composite
		if( TestPrime.isPrime(num) ) {
			return retval;
		}
		
		// Lets check
		while( prime < num && !retval ) {
			for( int square = 0; square <= num && !retval; square++ ) {
				retval = retval || num == (prime + (2 * square * square));
			}
			
			prime = TestPrime.getNextPrime( prime );
		}
		
		return retval;
	}
	
	public static void main( String[] args ) {
		int i = 1;
		boolean found = false;
		
		while( !found && i < 10000) {
			i += 2;
			
			if( isGoldbach(i) ) {
				System.out.println( "Goldbach: " + i );
			} else {
				if( !TestPrime.isPrime(i) ) {
					System.out.println( "Found: " + i );
					found = true;
				}
			}
		}
	}
}
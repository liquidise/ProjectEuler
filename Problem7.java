public class Problem7 {
	
	private static boolean isPrime( long num ) {
		boolean retval = true;
		int root;
		
		if( num ==2 || num == 3 ) {
			retval = true;
		} else if( num % 2 == 0 || num % 3 == 0 ) {
			retval = false;
		} else {
			root = (int) Math.floor( Math.sqrt(num) ) + 1;
			
			for( int i = 2; i < root && retval; i++ ) {
				retval = (num % i != 0);
			}
		}
		
		return retval;
	}
	
	public static void main( String[] args ) {
		int numPrimes = 1;
		int solution = 0;
		
		for( int i = 3; numPrimes <= 10001; i+=2 ) {
			if( isPrime(i) ) {
				// We want to know the high primes baby
				if( numPrimes > 9990 ) {
					System.out.println( "Prime number " + numPrimes + " is: " + i );
				}
				
				numPrimes++;			
			}
			
			
		}
	}
}
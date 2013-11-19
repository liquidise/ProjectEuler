public class Problem3 {
	final static double NUMBER = 600851475143d;
	
	private static boolean isPrime( double num ) {
		boolean retval = true;
		
		for( int i = 2; i < ((num/2) + 1) && retval; i++ ) {
			retval = (num % i != 0);
		}
		
		return retval;
	}
	
	public static void main( String[] args ) {
		double solution = 0;
		double quotient;
		
			
		// Find this nonsense
		for( double i = 2; i < NUMBER && solution < 1; i++ ) {
			
			if( NUMBER % i == 0 ) {
				quotient = NUMBER / i;
				
				if( isPrime(quotient) ) {
					solution = quotient;
				}
			}
		}
		
		// Print solution
		System.out.println( "The largest prime factor is: " + solution );
	}
}
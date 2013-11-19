public class Problem10 {
	
	private static boolean isPrime( long num ) {
		boolean retval = true;
		int root;
		
		if( num == 2 || num == 3 ) {
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
		long solution = 2;
		
		for( int i = 3; i < 2000000; i+=2 ) {
			if( isPrime(i) ) {
				solution += i;
			}
			
			if( i % 50000 == 1 ) {
				System.out.println( "Current Value: " + i + "  Current sum: " + solution );
			}
		}
		
		System.out.println( "The sum is: " + solution );
	}
}
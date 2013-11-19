public class Problem12 {
	
	static boolean has500Divisors( long num ) {
		int numDivisors = 2;
		int upperLimit = (int) num / 2;
		
		for( int i = 2; i < upperLimit + 1; i++ ) {
			if( num % i == 0 ) {
				numDivisors += 2;
				upperLimit = (int) num / i ;
			}
		}
		
		if( numDivisors > 200 ) {
			System.out.println( "" + num + " has " + numDivisors + " divisors." );
		}
		
		return numDivisors >= 500;
	}
	
	static long makeTriangle( int num ) {
		long triangle = 0l;
		
		for( int i = 1; i < num; i++ ) {
			triangle += i;
		}
		
		return triangle;
	}
	
	public static void main( String[] args ) {
		int solution = 0;
		long triangle = 0l;
		
		for( int i = 1; solution < 1; i++ ) {
			triangle = makeTriangle( i );
			
			if( has500Divisors(triangle) ) {
				solution = i;
			}
		}
		
		System.out.println( "The first triangle number is: " + triangle );
		
	}
}
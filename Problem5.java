public class Problem5 {
	
	static boolean isDivisible( int num ) {
		boolean retval = true;
		
		for( int i = 20; retval && i > 1; i-- ) {
			retval = num % i == 0;
		}
		
		return retval;
	}
	
	public static void main( String[] args ) {
		int solution = 0;
		
		for( int i = 20; solution < 1; i++ ) {
			if( isDivisible(i) ) {
				solution = i;
			}
		}
		
		System.out.println( "The lowest divisble number is: " + solution );
	}
}
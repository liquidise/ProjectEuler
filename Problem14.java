public class Problem14 {
	
	
	
	public static void main( String[] args ) {
		long startVal = 0;
		long curVal = 0;
		int numSteps = 0;
		int solutionSteps = 0;
		long solution = 0;
		
		// Loop starting values
		for( int i = 1; i < 1000000; i++ ) {
			startVal = i;
			curVal = startVal;
			numSteps = 0;
			
			// Loop this chain
			while( curVal > 1 ) {
				numSteps++;
				
				if( curVal % 2 == 0 ) {
					// Even: n = n / 2
					curVal = curVal / 2;
				} else {
					// Odd: n = 3n + 1
					curVal = (3 * curVal) + 1;
				}
			}
			
			// If this is better then current best
			if( numSteps > solutionSteps ) {
				solutionSteps = numSteps;
				solution = startVal;
				
				System.out.println( "New top - Start: " + startVal + 
				 					"   Num steps: " + numSteps );
			}
		}
		
		System.out.println( "Starting value is: " + solution );
		System.out.println( "Number of steps was: " + solutionSteps );
	}
}
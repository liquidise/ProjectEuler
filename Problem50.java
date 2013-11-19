public class Problem50 {
	private static final long LIMIT = 1000000;
	
	public static void main( String[] args ) {
		long num = 0;
		int consecutive = 0;
		int tempConsecutive = 0;
		long curPrime;
		long startingPrime = 2;
		long sum = 0;
		
		while( startingPrime <= LIMIT ) {
			curPrime = startingPrime;
			
			while( sum <= LIMIT ) {
				if(TestPrime.isPrime(sum) && consecutive < tempConsecutive) {
					System.out.println( "New found: ( " + sum + ", " + tempConsecutive + " )" );
					consecutive = tempConsecutive;
					num = sum;
				}
				
				sum += curPrime;
				tempConsecutive++;
				
				curPrime = TestPrime.getNextPrime( curPrime );
			}
			
			sum = 0;
			tempConsecutive = 0;
			startingPrime = TestPrime.getNextPrime( startingPrime );
		}
		
		System.out.println("Num = " + num + " using " + consecutive + " primes.");
	}
}
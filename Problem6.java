public class Problem6 {
	
	public static void main( String[] args ) {
		long sumOfSquares = 0;
		long squareOfSums = 0;
		long solution = 0;
		
		// Find sum of squares
		for( int i = 1; i <= 100; i++ ) {
			sumOfSquares += (i * i);
		}
		
		// Find square of sums
		for( int i = 1; i <= 100; i++ ) {
			squareOfSums += i;
		}
		squareOfSums *= squareOfSums;
		
		// Find Solution
		solution = squareOfSums - sumOfSquares;
		
		System.out.println( "Sum of Squares: " + sumOfSquares );
		System.out.println( "Square of sum: " + squareOfSums );
		System.out.println( "The difference is: " + solution );
	}
}
public class Problem28 {	
	public static void main( String[] args ) {
		long sum = 1;
		long topRight;
		
		for( int i = 3; i <= 1001; i+=2 ) {
			topRight = i * i;
			sum += (4 * topRight) - (6 * (i - 1));
		}
		
		System.out.println( "Sum = " + sum );
	}
}
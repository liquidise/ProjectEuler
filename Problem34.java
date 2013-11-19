import java.math.BigInteger;

public class Problem34 {
	private static long factorial( int num ) {
		for( int i = num - 1; i > 1; i-- ) {
			num *= i;
		}
		
		return num != 0 ? num : 1;
	}
	
	private static boolean factorialsEqual( long num ) {
		long sum = 0;
		
		for( long i = 10; i < (10 * num); i *= 10 ) {
			sum += factorial( (int) ((num % i) / (i / 10)) );
		}
		
		return sum == num;
	} 
	
	public static void main( String[] args ) {
		BigInteger totalSum = new BigInteger("0");
		long i = 0;
		
		for( i = 3; i < 9999999; i++ ) {
			if( i % 100000 == 3 ) {
				System.out.println( "Calculating for i = " + i + "..." );
				System.out.println( "Current Sum = " + totalSum );
			}
			
			if( factorialsEqual(i) ) {
				totalSum = totalSum.add( BigInteger.valueOf(i) );
			}
		}
		
		System.out.println( "Sum = " + totalSum );
	}
}
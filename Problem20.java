import java.math.BigInteger;

public class Problem20 {
	
	public static void main( String[] args ) {
		BigInteger num = BigInteger.TEN;
		String factorial;
		int sum = 0;
		
		num = num.multiply( BigInteger.TEN );
		
		// Compute Factorial
		for( int i = 99; i > 1; i-- ) {
			num = num.multiply( new BigInteger(""+i) );
		}
		
		factorial = num.toString();
		
		for( int i = 0; i < factorial.length(); i++ ) {
			sum += Integer.parseInt( "" + factorial.charAt(i) );
		}
		
		System.out.println( "" + sum );
	}
}
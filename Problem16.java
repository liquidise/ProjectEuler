import java.math.BigInteger;

public class Problem16 {
	
	public static void main( String[] args ) {
		BigInteger num = BigInteger.ONE;
		String power;
		int sum = 0;
		
		num = num.add( BigInteger.ONE );
		num = num.pow( 1000 );
		power = num.toString();
		
		for( int i = 0; i < power.length(); i++ ) {
			sum += Integer.parseInt( "" + power.charAt(i) );
		}
		
		System.out.println( "" + sum );
	}
}
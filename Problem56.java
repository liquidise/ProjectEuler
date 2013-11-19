import java.math.BigInteger;

public class Problem56 {
	private static int sumDigits( BigInteger number ) {
		String num = number.toString();
		int sum = 0;
		
		for( int i = 0; i < num.length(); i++ ) {
			sum += Integer.parseInt("" + num.charAt(i));
		}
		
		return sum;
	}
	
	public static void main( String[] args ) {
		int max = 0;
		int temp = 0;
		String output = "";
		
		for( int a = 1; a < 100; a++ ) {
			for( int b = 1; b < 100; b++ ) {
				temp = sumDigits( BigInteger.valueOf(a).pow(b) );
				if( temp > max ) {
					max = temp;
					output = "a = " + a + ", b = " + b;
				}
			}
		}
		
		System.out.println( "max = " + max + "\n" + output );
	}
}
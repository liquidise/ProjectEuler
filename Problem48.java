import java.math.BigInteger;

public class Problem48 {	
	public static void main( String[] args ) {
		BigInteger num = null;
		BigInteger sum = new BigInteger("0");
		
		for( int i = 1; i < 1000; i++ ) {
			num = new BigInteger( "" + i );
			num = num.pow(i);
			sum = sum.add(num);
		//	System.out.println( "-------------\n" + i + "^" + i + " = " + num );
		}
		
		System.out.println( "sum = " + sum );
	}
}
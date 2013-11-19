import java.math.BigInteger;

public class Problem206 {
	
	public static void main( String[] args ) {
		BigInteger[] values = { 
						new BigInteger( "1020304050607080900" ),
						new BigInteger( "1121314151617181910" ),
						new BigInteger( "1222324252627282920" ),
						new BigInteger( "1323334353637383930" ),
						new BigInteger( "1424344454647484940" ),
						new BigInteger( "1525354555657585950" ),
						new BigInteger( "1626364656667686960" ),
						new BigInteger( "1727374757677787970" ),
						new BigInteger( "1828384858678888980" ),
						new BigInteger( "1929394959697989990" )
					};
		BigInteger num = new BigInteger("1000000000");
		BigInteger printOn = new BigInteger("1000000");
		BigInteger one = BigInteger.valueOf(1);
		BigInteger approx = new BigInteger("100000");
		BigInteger temp = num;
		
		// Loop over the possibel values
		for( int i = 0; i < values.length; i++ ) {
			// Approximate the sqrt
			while( temp.compareTo(values[i]) == -1 ) {
				num = num.add( approx );
				temp = num.pow( 2 );
			}
			
			num = num.subtract( approx );
			temp = num.pow( 2 );
			
			System.out.println( "Checking value #" + i + "\nStarting with: " + num + "\nSquare = " + temp );
			
			// Check the sqrt for that value
			while( temp.compareTo(values[i]) < 1 ) {
				num = num.add( one );
				temp = num.pow( 2 );
				
				if( temp.compareTo(values[i]) == 0 ) {
					System.out.println( "Num = " + temp );
					return;
				}
			}
			
			System.out.println( "\nLast Check = " + num + "\nSquare = " + temp + "");
			num = num.subtract( one );
			temp = num.pow( 2 );
			System.out.println( "Prev Check = " + num + "\nSquare = " + temp + "\n---------------\n");
		}
	}
}
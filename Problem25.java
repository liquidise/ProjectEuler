import java.math.BigInteger;

public class Problem25 {
	private static BigInteger curVal = new BigInteger("1");
	private static BigInteger lastVal = new BigInteger("0");
	
	public static void main( String[] args ) {
		BigInteger temp = null;
		int lessThan = 1;
		int i = 1;
		String digitCount = "";
		BigInteger tenDigits = (new BigInteger("10")).pow(999);
		
		for( i = 1; lessThan > 0; i++ ) {
			if( i % 100 == 1 ) {
				System.out.println( "-------------\nF(" + i + ") = " + curVal );
				digitCount = curVal.toString();
				System.out.println( "Digits = " + digitCount.length() );
			}
			
			temp = curVal;
			curVal = curVal.add( lastVal );
			lastVal = temp;
			
			lessThan = tenDigits.compareTo(curVal);
		}
		
		System.out.println( "-------------\nF(" + i + ") = " + curVal );
		digitCount = curVal.toString();
		System.out.println( "Digits = " + digitCount.length() );
	}
}
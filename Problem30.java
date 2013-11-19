public class Problem30 {	
	public static void main( String[] args ) {
		long totalSum = 0;
		long sum = 0;
		String num;
		int curDigit = 0;
				
		// Skip 1
		for( long i = 2; i < 1000000; i++ ) {
			num = "" + i;
			
			for( int j = 0; j < num.length(); j++ ) {
				curDigit = Integer.parseInt( "" + num.charAt(j) );
				sum += (int) Math.pow( curDigit, 5 );
			}
			
			if( sum == i ) {
				totalSum += sum;
			}
			
			sum = 0;
		}
		
		System.out.println( "sum = " + totalSum );
	}
}
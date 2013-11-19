public class Problem2 {
	final static double MAX = 4000000;
	
	public static void main( String[] args ) {
		double sum = 0;
		
		double num1 = 1;
		double num2 = 2;
		double temp;
		
		while( num2 < MAX ) {
			// add if even
			if( num2 % 2 == 0 ) {
				sum += num2;
			}
			
			// get next number
			temp = num2;
			num2 += num1;
			num1 = temp;
		}
		
		System.out.println( "The answer is " + sum );
	}
}
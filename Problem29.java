// top right = 1001 * 1001 = 1002001

public class Problem28 {	
	public static void main( String[] args ) {
		long sum = 1;
		long topRight;
		
		for( int i = 3; i <= 5; i+=2 ) {
			topRight = i * i;
			sum += topRight;
			sum += topRight - (i - 1);
			sum += topRight - (2 * (i - 1));
			sum += topRight - (3 * (i - 1));
		}
		
		System.out.println( "Sum = " + sum );
	}
}
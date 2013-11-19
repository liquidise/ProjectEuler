public class Problem9 {
	
	static boolean isTriple( int a, int b, int c ) {
		return (a*a) + (b*b) == (c*c);
	}
	
	public static void main( String[] args ) {
		
		for( int a = 1; a < 333; a++ ) {
			for( int b = a + 1; b < 400; b++ ) {
				for( int c = b + 1; c < 500; c++ ) {
					if( a + b + c == 1000 & isTriple(a, b, c) ) {
						System.out.println( "The triple is: a = " + a + " b = " + b + " c = " + c );
						System.out.println( "The product is: " + a*b*c );
					}
				}
			}
		}
	}
}
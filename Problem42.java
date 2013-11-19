public class Problem42 {
	private int[] triangles = {1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 05, 20, 36, 53, 71, 190};
	
	public static void main( String[] args ) {
		int triange = 0;
		
		for( int i = 1; i < 20; i++ ) {
			triange = (i * (i + 1)) / 2;
			System.out.println( triange );
		}
	}
}
public class Problem24 {
	//static int[] number = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
	//static int[] number = {0, 1, 2, 3, 4};
	static int[] number = {0, 1, 2};
	
	
	static String printNum() {
		String retval = "";
		
		for( int i = 0; i < number.length; i++ ) {
			retval += number[i];
		}
		
		return retval;
	}
	
	
	public static void main( String[] args ) {
		int[] tempSet = new int[number.length];
		double iteration = 0;
		int temp;
		
		
		// Permutate
		for( int i = 0; i < number.length; i++ ) {
			// Save current ordering
			tempSet = number;
			
			// Other Shit
			
			// Swap number[0]
			temp = tempSet[0];
			tempSet[0] = tempSet[1];
			tempSet[1] = temp;
			
			number = tempSet;
		}
		
		System.out.println( "The number is: " + printNum() );
	}
}
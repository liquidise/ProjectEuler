public class Problem36 {
	private static boolean isPalindrome( String string ) {
		for( int i = 0; i < (int)(string.length() / 2); i++ ) {
			if( string.charAt(i) != string.charAt(string.length() - 1 - i) ) {
				return false;
			}
		}
		
		return true;
	}
	
	public static void main( String[] args ) {
		long sum = 0;
		long i = 0;
		
		for( i = 0; i < 1000000; i++ ) {
			if( isPalindrome("" + i) && isPalindrome(Long.toBinaryString(i)) ) {
				sum += i;
				System.out.println("Adding: " + i);
			}
		}
		
		System.out.println("Sum = " + sum);
	}
}
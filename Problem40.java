public class Problem40 {
	private static boolean isPalindrome( String string ) {
		for( int i = 0; i < (int)(string.length() / 2); i++ ) {
			if( string.charAt(i) != string.charAt(string.length() - 1 - i) ) {
				return false;
			}
		}
		
		return true;
	}
	
	public static void main( String[] args ) {
		String num = "";
		long i = 0;
		
		for( i = 0; i < 200000; i++ ) {
			num += i;
		}
		
		System.out.println("Num = " + num.charAt(1));
		System.out.println("Num = " + num.charAt(10));
		System.out.println("Num = " + num.charAt(100));
		System.out.println("Num = " + num.charAt(1000));
		System.out.println("Num = " + num.charAt(10000));
		System.out.println("Num = " + num.charAt(100000));
		System.out.println("Len = " + num.length());
		System.out.println("Num = " + num.charAt(1000000));
	}
}
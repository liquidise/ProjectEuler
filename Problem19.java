public class Problem19 {
	static int[] DAYS_OF_MONTH = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

	public static void main( String[] args ) {
		int daysThisYear = 1;
		int sundays = 0;
		int modulus = 6;

		for( int year = 1901; year < 2001; year++ ) {

			for( int month = 0; month < 12; month++ ) {
				if( daysThisYear % 7 == modulus ) {
					sundays++;
				}

				daysThisYear += DAYS_OF_MONTH[month];

				// Tack on another day for leap year
				if( month == 1 ) {
					if( (year % 4 == 0 && year % 100 != 0) || year % 400 == 0 ) {
						daysThisYear += 1;
					}
				}
			}

			daysThisYear = 1;
			modulus = (modulus - 1) % 7;

			if( modulus < 0 ) {
				modulus = modulus + 7;
			}
		}

		System.out.println( "" + sundays );
	}
}
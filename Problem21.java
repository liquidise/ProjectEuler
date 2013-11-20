public class Problem21 {
	static int MAX = 10000;
	static int[] used = new int[10000];
	static int index = 0;

	static int sumOfDivisors( int num ) {
		int retval = 1;

		for( int i = 2; i <= num/2; i++ ) {
			if( num % i == 0 ) {
				retval += i;
			}
		}

		return retval;
	}

	static boolean isAmicable( int num ) {
		boolean retval = false;
		int sum1 = sumOfDivisors(num);
		int sum2 = sumOfDivisors(sum1);

		if( sum1 != sum2 && num == sum2 ) {
			retval = true;
			used[index++] = num;
			used[index++] = sum2;
		}

		return retval;
	}

	static boolean hasBeenUsed( int num ) {
		boolean retval = false;

		for( int i = 0; !retval && i < index; i++ ) {
			if( used[i] == num ) {
				retval = true;
			}
		}

		return retval;
	}

	public static void main( String[] args ) {
		long sum = 0l;
		int num1 = 0;
		int num2 = 0;

		for( int i = 0; i < MAX; i++ ) {
			if( !hasBeenUsed(i) && isAmicable(i) ) {
				sum += i;
			}
		}

		System.out.println( "The sum is: " + sum );
	}
}
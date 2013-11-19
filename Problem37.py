from number_theory import isPrime

def contains_even( number ):
    str_number = str( number )
    if str_number.find( '2' ) > 0:
        return True

    for i in str_number:
        if i in ['4', '6', '8', '0']:
            return True
    return False


number = 11
found = 0

total_sum = 0
while found < 11:
    number += 2

    if contains_even( number ):
        continue

    if isPrime( number ):
        str_prime = str( number )
        num_digits = len( str_prime )

        # Left to right
        is_truncatable = True
        for i in range( 0, num_digits ):
            shorter_number = int( str_prime[i:] )
            if not isPrime( shorter_number ):
                is_truncatable = False
                break

            if i > 0:
                shorter_number = int( str_prime[:i] )
                if not isPrime( shorter_number ):
                    is_truncatable = False
                    break

        if is_truncatable:
            found += 1
            total_sum += number
            print "FOUND " + str(number)

print "\n\nTotal: " + str( total_sum )
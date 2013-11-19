def calcPentagonal( number ):
    return number * (3 * number - 1) / 2


def isPentagonal( number ):
    try:
        return hash_numbers[ number ]
    except Exception as e:
        return False


numbers = []
hash_numbers = {}

for i in range( 1, 2500 ):
    number = calcPentagonal( i )
    hash_numbers[ number ] = True
    numbers.append( number )


step_size = 1000
while step_size < 2000:
    print "Step Size: " + str( step_size )

    for i in range( 0, len(numbers) - step_size ):

        number_sum = numbers[i] + numbers[i + step_size]
        if isPentagonal( number_sum ):
            print "  +", numbers[i], numbers[i + step_size]
        else:
            continue

        diff = numbers[i + step_size] - numbers[i]
        if isPentagonal( diff ):
            print "  -", numbers[i], numbers[i + step_size]

        if isPentagonal( diff ) and isPentagonal( number_sum ):
            print "  ", "FOUND", numbers[i], numbers[i + step_size]
            exit()

    step_size += 1

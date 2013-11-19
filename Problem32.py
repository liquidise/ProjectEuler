numbers = ['1','2','3','4','5','6','7','8','9']

def contain_all_digits( num1, num2, num3 ):
    number = str( num1 ) + str( num2 ) + str( num3 )

    if len(number) != 9:
        return False

    for i in numbers:
        if number.count( i ) != 1:
            return False

    return True


def are_all_uniq_digits( num1, num2, num3=None ):
    num1 = str( num1 )
    num2 = str( num2 )

    if num3:
        num3 = str( num3 )

    # Search for num1 digits in num2
    for char in num1:
        if num1.count( char ) > 1 or num2.find( char ) >= 0:
            return False
        if num3 and num3.find( char ) >= 0:
            return False

    # Search for num2 digits in num1
    for char in num2:
        if num2.count( char ) > 1 or num1.find( char ) >= 0:
            return False
        if num3 and num3.find( char ) >= 0:
            return False

    if num3:
        for char in num3:
            if num3.count( char ) > 1:
                return False

    return True





first_num = 0
second_num = 0
product = 0

valid = 0
invalid = 0

products = []
total_sum = 0
for first in range( 2, 9876 ):
    for second in range( 2, 988 ):
        if are_all_uniq_digits( first, second ):
            product = first * second
            if products.count( product ) == 0:
                if contain_all_digits( first, second, product ) and are_all_uniq_digits( first, second, product):
                    products.append( product )
                    print first, second, product
                    total_sum += product

print total_sum

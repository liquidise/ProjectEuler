for numerator in range( 10, 99 ):
    for denominator in range( 10, 99 ):
        if numerator == denominator:
            continue

        str_num1 = str( numerator )
        str_num2 = str( denominator )

        trial_numerator = str_num1.replace( str_num1[0], '' )
        trial_denominator = str_num2.replace( str_num1[0], '' )

        if trial_numerator:
            trial_numerator = int( trial_numerator )
        else:
            continue

        if trial_denominator and trial_denominator != '0':
            trial_denominator = int( trial_denominator )
        else:
            continue

        if float(numerator) / denominator == float(trial_numerator) / trial_denominator:
            print numerator, denominator, numerator/denominator, trial_numerator / trial_denominator
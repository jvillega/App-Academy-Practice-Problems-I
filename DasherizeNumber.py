#!/usr/bin/env python3

# Write a method that takes in a number and returns a string, placing
# a single dash before and after each odd digit. There is one
# exception: don't start or end the string with a dash.
#
# You may wish to use the `%` modulo operation; you can see if a number
# is even if it has zero remainder when divided by two.
#
# Difficulty: medium.

def dasherizeNumber( num ):

    updateNum = ""

    for x in str( num ):
        if int( x )%2 == 1:
            if str( num ).find( x ) == len( str( num ) ) - 1:
                updateNum = updateNum + "-" + x
            elif str( num ).find( x ) == 0:
                updateNum = updateNum + x + "-"

            else:
                updateNum = updateNum + "-" + x + "-"

        else:
            updateNum = updateNum + x

    return updateNum


print( dasherizeNumber( 4236 ) )
print( dasherizeNumber( 32686 ) )
print( dasherizeNumber( 423 ) )

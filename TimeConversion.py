#!/usr/bin/env python3

# Write a method that will take in a number of minutes, and returns a
# string that formats the number into `hours:minutes`.
#
# Difficulty: easy.


# Precondition: minutes is a defined int
# Postcondition: minutes converted to hh:mm format returned
def timeConversion( minutes ):
    hours = minutes//60
    minutes = (minutes%60)
    
    if minutes < 10:
        return str( hours ) + ":0" + str( minutes )
    else:
        return str( hours ) + ":" + str( minutes )


print( timeConversion( 150 ) )
print( timeConversion( 15 ) )
print( timeConversion( 360 ) )
print( timeConversion( 420 ) )
print( timeConversion( 7 ) )
print( timeConversion( 157 ) )

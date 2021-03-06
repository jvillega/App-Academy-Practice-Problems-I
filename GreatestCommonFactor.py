#!/usr/bin/env python3

# Write a method that takes in two numbers. Return the greatest
# integer that evenly divides both numbers. You may wish to use the
# `%` modulo operation.
#
# Difficulty: medium.

# Precondition: numberOne or numberTwo != 0
# Postcondition: GCF of numberOne and numberTwo returned
def greatestCommonFactor( numberOne, numberTwo ):

    curGCF = 0

    # Uncomment to test for 0
#    if numberOne == 0:
#        return 0
#    if numberTwo == 0:
#        reutrn 0
    
    if numberOne < numberTwo:
        for index in range( numberOne - 2 ):
            if numberOne % ( index + 2 ) == 0:
                if numberTwo % ( index + 2 ) == 0:
                    if ( index + 2 ) > curGCF:
                        curGCF = index + 2

        if curGCF == 0:
            if numberTwo % numberOne == 0:
                curGCF = numberOne
            else:
                curGCF = 1

    else:
        for index in range( numberTwo - 2 ):
            if numberOne % ( index + 2 ) == 0:
                if numberTwo % ( index + 2 ) == 0:
                    if ( index + 2 ) > curGCF:
                        curGCF = index + 2
                    else:
                        curGCF = numberTwo

        if curGCF == 0:
            if numberOne % numberTwo == 0:
                curGCF = numberTwo
            else:
                curGCF = 1

    return curGCF

# These are tests to check that your code is working. After writing
# your solution, they should all print true.

print( greatestCommonFactor(3, 9) )
print( greatestCommonFactor(16, 24) )
print( greatestCommonFactor(3, 5) )
print( greatestCommonFactor(4, 15) )
print( greatestCommonFactor(4, 1) )
print( greatestCommonFactor(4, 2) )

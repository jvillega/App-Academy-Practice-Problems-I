#!/usr/bin/env python3

# Write a method that takes in an integer `num` and returns the sum of
# all integers between zero and num, up to and including `num`.
#
# Difficulty: easy.


# Precondition: num is a defined integer
# Postcondition: sum of all integers between zero and num are returned
def sumNums( num ):

    total = 0
    
    for x in range( num + 1 ):
        total += x
        
    return total

print( sumNums( 6 ) )
print( sumNums( 5 ) )

#!/usr/bin/env python3

# Write a method that takes in an integer (greater than one) and
# returns true if it is prime; otherwise return false.
#
# You may want to use the `%` modulo operation. `5 % 2` returns the
# remainder when dividing 5 by 2; therefore, `5 % 2 == 1`. In the case
# of `6 % 2`, since 2 evenly divides 6 with no remainder, `6 % 2 == 0`.
# More generally, if `m` and `n` are integers, `m % n == 0` if and only
# if `n` divides `m` evenly.
#
# You would not be expected to already know about modulo for the
# challenge.
#
# Difficulty: medium.

def isPrime( number ):

    if number == 2:
        return True

    for count in range( number - 2 ):
        if number % ( count + 2 ) == 0:
            return False

    return True
    

# These are tests to check that your code is working. After writing
# your solution, they should all print true.

print( isPrime( 2 ) )
print( isPrime( 14 ) )
print( isPrime( 5 ) )
print( isPrime( 3 ) )
print( isPrime( 4 ) )
print( isPrime( 9 ) )
print( isPrime( 659 ) )

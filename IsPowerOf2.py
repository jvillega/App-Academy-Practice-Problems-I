#!/usr/bin/env python3

# Write a method that takes in a number and returns true if it is a
# power of 2. Otherwise, return false.
#
# You may want to use the `%` modulo operation. `5 % 2` returns the
# remainder when dividing 5 by 2; therefore, `5 % 2 == 1`. In the case
# of `6 % 2`, since 2 evenly divides 6 with no remainder, `6 % 2 == 0`.
#
# Difficulty: medium.

def isPowerOfTwo(num):
    if num == 0:
        return False
    while num != 0:
        if num == 1:
            return True
        if num%2 != 0:
            return False
        num = num/2

print( isPowerOfTwo( 1 ) )
print( isPowerOfTwo( 16 ) )
print( isPowerOfTwo( 15 ) )
print( isPowerOfTwo( 78 ) )
print( isPowerOfTwo( 0 ) )
print( isPowerOfTwo( 64 ) )
print( isPowerOfTwo( 128 ) )

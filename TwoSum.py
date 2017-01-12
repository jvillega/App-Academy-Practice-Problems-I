#!/usr/bin/env python3

# Write a method that takes an array of numbers. If a pair of numbers
# in the array sums to zero, return the positions of those two numbers.
# If no pair of numbers sums to zero, return `nil`.
#
# Difficulty: medium.

def twoSum( nums ):
    for x in range( len( nums ) ):
        if ( x ) == len( nums ) - 1:
            return None
        else:
            if nums[ x ] + nums[ x + 1 ] == 0:
                return[ x, x + 1 ]


print( twoSum( [6,7,8,9,63,15,-15,45] ) )
print( twoSum( [1548, -1548, 6598, 36, 1, 2] ) )
print( twoSum( [1548, 1548, 6598, 36, 1, 2] ) )
print( twoSum( [6,7,8,9,63,15,-45,45] ) )

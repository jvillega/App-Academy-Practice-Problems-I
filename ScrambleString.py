#!/usr/bin/env python3

# Write a method that takes in a string and an array of indices in the
# string. Produce a new string, which contains letters from the input
# string in the order specified by the indices of the array of indices.
#
# Difficulty: medium.

def scrambleString( string, positions ):

    newString = ""

    for position in positions:
        newString = newString + string[ position ] 

    return newString

print( scrambleString( "abcd", [ 3, 1, 2, 0 ] ) )
print( scrambleString( "markov", [ 5, 3, 1, 4, 2, 0 ] ) )

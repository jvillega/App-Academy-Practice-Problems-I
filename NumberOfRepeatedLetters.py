#!/usr/bin/env python3

# Write a method that takes in a string and returns the number of
# letters that appear more than once in the string. You may assume
# the string contains only lowercase letters. Count the number of
# letters that repeat, not the number of times they repeat in the
# string.
#
# Difficulty: hard.

def numRepeats( string ):

    charsInString = {}
    numRepeats = 0

    for char in string:
        if charsInString.get( char ) == None:
            charsInString[ char ] = 1
        else:
            charsInString[ char ] =  charsInString.get( char ) + 1

    for key in charsInString:
        if charsInString.get( key ) > 1:
            numRepeats += 1

    return numRepeats

# These are tests to check that your code is working. After writing
# your solution, they should all print true.
print( numRepeats( 'abdbc' ) )
print( numRepeats('aaa') )
print( numRepeats('abab') )
print( numRepeats('cadac') )
print( numRepeats('abcde') )

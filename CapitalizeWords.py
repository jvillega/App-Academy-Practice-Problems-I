#!/usr/bin/env python3

# Write a method that takes in a string of lowercase letters and
# spaces, producing a new string that capitalizes the first letter of
# each word.
#
# You'll want to use the `split` and `join` methods. Also, the String
# method `upcase`, which converts a string to all upper case will be
# helpful.
#
# Difficulty: medium.

def capitalizeWords( string ):

    splitString = string.split( " " )

    newString = ""

    for index in range( len( splitString ) ):
        curWord = splitString[ index ]
        splitString[ index ] = curWord[ 0 : 1 ].upper() + curWord[ 1: ]

    for index in range( len( splitString ) ):
        if index == len( splitString ) - 1:
            newString = newString + splitString[ index ]
        else:
            newString = newString + splitString[ index ] + " "

    return newString
  
print( capitalizeWords( "hello, world! this is a testString!" ) )

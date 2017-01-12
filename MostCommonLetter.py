#!/usr/bin/env python3

# Write a method that takes in a string. Your method should return the
# most common letter in the string, and a count of how many times it
# appears.
#
# Difficulty: medium.

def mostCommonLetter( string ):
    alphabetDict = { 'a': 0 }
    tempAlphabetDict = dict( alphabetDict )
    total = 0

    for char in string:
        for key in alphabetDict:
            if key == char:
                total = tempAlphabetDict[ key ]
                tempAlphabetDict[ key ] = total + 1
                flag = 0
                break
            else:
                flag = 1
        if flag == 1:
            tempAlphabetDict[ char ] = 1

        alphabetDict = dict( tempAlphabetDict )

    total = -1

    for key in alphabetDict:
        if alphabetDict[ key ] > total:
            total = alphabetDict[ key ]
            largestKey = key

    return largestKey, alphabetDict[ largestKey ]

print( mostCommonLetter( "abaad" ) )
print( mostCommonLetter( "cdaccpld" ) )
print( mostCommonLetter( "asasasddddd" ) )
print( mostCommonLetter( "kfjdjhdfdfadfadsfasdfasdfasdfasdffffffddhhhhhh" ) )

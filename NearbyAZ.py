#!/usr/bin/env python3

# Write a method that takes a string in and returns true if the letter
# "z" appears within three letters **after** an "a". You may assume
# that the string contains only lowercase letters.
#
# Difficulty: medium.

def nearbyAZ(string):

    indexOfA = string.find( 'a' )

    if indexOfA < 0:
        return False

    disToSearch = len( string ) - indexOfA

    if disToSearch > 3:
        disToSearch == 3

    for index in range( disToSearch - 1 ):
        if string[index + indexOfA + 1] == 'z':
            return True
    return False
            
    
print( nearbyAZ( 'baz' ) )
print( nearbyAZ( 'abz' ) )
print( nearbyAZ('abcz') )
print( nearbyAZ('a') )
print( nearbyAZ('z') )
print( nearbyAZ('za') )

#!/usr/bin/env python3

# Write a method that takes in a string. Return the longest word in
# the string. You may assume that the string contains only letters and
# spaces.
#
# You may use the String `split` method to aid you in your quest.
#
# Difficulty: easy.

def longestWord( string ):
    
    curSpace = 0
    prevSpace = 0
    longestWord = ""
    
    # Loop through string
    for curIndex in range( len( string ) ):
        if string[ curIndex ] == " ":
            curSpace = curIndex
            if curSpace > prevSpace:
                if len( longestWord ) < ( curSpace - prevSpace ):
                    longestWord = string[ prevSpace : curSpace ]
                prevSpace = curSpace + 1

    return longestWord

print( longestWord( "abc def dfda " ) )
print( longestWord( "abc def lkjhgfdsa dfda " ) )
print( longestWord( "abc compilerdef lkjhgfdsa dfda " ) )
print( longestWord( "fasdfdasfdaabc compilerdef lkjhgfdsa dfda " ) )
print( longestWord( "abc compilerdef lkjhgfdsa dfda gfafgfwerterfv " ) )

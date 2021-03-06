#!/usr/bin/env python3

# Write a method that takes in a string of lowercase letters (no
# uppercase letters, no repeats). Consider the *substrings* of the
# string: consecutive sequences of letters contained inside the string.
# Find the longest such string of letters that is a palindrome.
#
# Note that the entire string may itself be a palindrome.
#
# You may want to use Array's `slice(start_index, length)` method,
# which returns a substring of length `length` starting at index
# `start_index`:
#
#     "abcd".slice(1, 2) == "bc"
#     "abcd".slice(1, 3) == "bcd"
#     "abcd".slice(2, 1) == "c"
#     "abcd".slice(2, 2) == "cd"
#
# Difficulty: hard.

def isPalindrome( string ):
    if string == string[ : : -1 ]:
        return True

    else:
        return False

def longestPalindrome( string ):

    length = len( string )
    actualLongestPalindrome = ""

    for outerIndex in range( length  - 1 ):
        length = len( string )

        for innerIndex in range( length - outerIndex ):
            if isPalindrome( string[ outerIndex : length ] ) == True:
                if len( actualLongestPalindrome ) < len( string[ outerIndex : length ] ):
                    actualLongestPalindrome = string[ outerIndex : length ]
            length -= 1

    return actualLongestPalindrome

    
# These are tests to check that your code is working. After writing
# your solution, they should all print true.
print( longestPalindrome('abcbd') )
print( longestPalindrome('abba') )
print( longestPalindrome('abcbdeffe') )

#!/usr/bin/env python3

# Write a method that will take a string as input, and return a new
# string with the same letters in reverse order.
#
# Don't use String's reverse method; that would be too simple.
#
# Difficulty: easy.

def reverse(string):
    
    return string[ : : -1 ]

# These are tests to check that your code is working. After writing
# your solution, they should all print true.

print( reverse( "abc" ) )
print( reverse( "a" ) )
print( reverse( "" ) )  

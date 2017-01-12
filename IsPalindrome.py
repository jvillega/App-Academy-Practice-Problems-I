#!/usr/bin/env python3

# Write a method that takes a string and returns true if it is a
# palindrome. A palindrome is a string that is the same whether written
# backward or forward. Assume that there are no spaces; only lowercase
# letters will be given.
#
# Difficulty: easy.

def isPalindrome( string ):
	if string == string[ : : -1 ]:
		return True
	else:
		return False

print( isPalindrome( "hannah" ) )
print( isPalindrome( "racecar" ) )
print( isPalindrome( "hello" ) )

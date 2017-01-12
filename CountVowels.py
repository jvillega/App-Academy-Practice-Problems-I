#!/usr/bin/env python3

# Write a method that takes a string and returns the number of vowels
# in the string. You may assume that all the letters are lower cased.
# You can treat "y" as a consonant.
#
# Difficulty: easy.

def countVowels( string ):
    string = string.lower()

    vowels = ["a", "e", "i", "o", "u"]

    count = 0

    for x in string:
        for y in vowels:
            if x == y:
                count += 1
				
    return count
	

print( countVowels( "cecilia" ) )
print( countVowels( "Race Car" ) )

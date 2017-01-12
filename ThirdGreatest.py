#!/usr/bin/env python3

# Write a method that takes an array of numbers in. Your method should
# return the third greatest number in the array. You may assume that
# the array has at least three numbers in it.
#
# Difficulty: medium.

# Precondition: nums is a list of integers with at least three distinct values
# Postcondition: third largest integer in nums is returned
def thirdGreatest( nums ):

    sortedList = []

    for x in range( len( nums ) ):
        # insert first num into sortedList
        if x == 0:
            sortedList.insert( 0, nums[ x ] )
        # perform bubble sort
        else:
            # loop through current sortedList
            for y in range( len( sortedList ) ):
                # Skip duplicates
                if sortedList.count( nums[ x ] ) > 0:
                    break
                # is new num greater than current sortedList index
                elif nums[ x ] < sortedList[ y ]:
                    sortedList.insert( y, nums[ x ] )
                    break
                # if at the end of sortedList, append new num
                elif y == len( sortedList ) - 1:
                    sortedList.append( nums[ x ] )
                    break
    return sortedList[ len( sortedList ) - 3 ]  

print( thirdGreatest( [ 15, 6, 18 ] ) )		
print( thirdGreatest( [ 1, 2, 3 ] ) )
print( thirdGreatest( [ 1, 5, 6, 6, 4 ] ) )
print( thirdGreatest( [ 42, 5, 90, 234, 4, 19, 5, 6, 6, 4 ] ) )

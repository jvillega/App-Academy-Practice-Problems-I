#!/usr/bin/env python3

# Write a method that returns the `n`th prime number. Recall that only numbers greater than 1 can be prime.
#
# Difficulty: medium.

def isPrime( number ):

    if number == 2:
        return True

    for count in range( number - 2 ):
        if number % ( count + 2 ) == 0:
            return False

    return True
    
def nthPrime( number ):

    primeNumCount = 0
    curNum = 1

    while primeNumCount != number:
        curNum += 1

        if isPrime( curNum ) == True:
            primeNumCount += 1

    return curNum
  
print( nthPrime( 1 ) )
print( nthPrime( 2 ) )
print( nthPrime( 3 ) )
print( nthPrime( 4 ) )
print( nthPrime( 5 ) )
print( nthPrime( 15 ) )

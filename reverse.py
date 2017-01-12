#!/usr/bin/env python3

import math

def factoral( num ):
    
    total = 1
    
    if num == 0:
        return 1

    for x in range( num ):

        total = (x+1)*total

    return total

print( factoral( 6 ) )
print( factoral( 3 ) )
print( factoral( 4 ) )
print( factoral( 10 ) )

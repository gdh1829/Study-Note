"""
https://www.hackerrank.com/challenges/apple-and-orange/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s staring point of sam's house location
#  2. INTEGER t end point of sam's
#  3. INTEGER a apple tree location
#  4. INTEGER b orange tree location
#  5. INTEGER_ARRAY apples distances at which each apples fall from its tree.
#  6. INTEGER_ARRAY oranges distances at which each orages fall from its tree.
#

def isInHouse(fruit_distance, tree_location, house_start, house_end):   
    return True if (s <= (fruit_distance + tree_location) <= t) else False

def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple_cnt = 0
    orange_cnt = 0
    
    for distance in apples:
        if (isInHouse(distance, a, s, t)):
            apple_cnt += 1
    
    for distance in oranges:
        if (isInHouse(distance, b, s, t)):
            orange_cnt += 1

    print(apple_cnt)
    print(orange_cnt)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)

"""
https://www.hackerrank.com/challenges/diagonal-difference/problem
"""
#!/bin/python3

import math
import os
import random
import re
import sys
from functools import reduce

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def makeSum(values):
    return reduce(lambda acc, val: acc + val, values, 0)

def diagonalDifference(arr):
    left_to_right_diagonals = []
    right_to_left_diagonals = []
    size = len(arr)
    
    for i in range(size):
        left_to_right_diagonals.append(arr[i][i])
        right_to_left_diagonals.append(arr[i][size-1-i])
    
    return abs(makeSum(left_to_right_diagonals) - makeSum(right_to_left_diagonals))
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

"""
https://www.hackerrank.com/challenges/mini-max-sum/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys
from functools import reduce

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    total = reduce(lambda acc, val: acc + val, arr, 0)
    sums = []
    for ele in arr:
        sums.append(total - ele)
    
    print(f'{min(sums)} {max(sums)}')

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

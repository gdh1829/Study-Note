"""
https://www.hackerrank.com/challenges/picking-numbers/problem
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    longest_length = 0
    distinct_a = set(a)
    
    
    # 1 3 4 5 6
    for i in distinct_a:
        print('@@1', i)
        current_length = 0
        elements = {i}
        
        # each i number combination
        for j in distinct_a:
            # first check between two elements
            if abs(i - j) == 1:
                # second check within current combination
                if all(abs(j - k) == 1 for k in elements):
                    elements.add(j)
                     
        # each i number total length
        for ele in elements:
            if a.count(ele) >= 1:
                current_length += a.count(ele)
                
        if longest_length < current_length:
            longest_length = current_length

    return longest_length

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()

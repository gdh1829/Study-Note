"""
https://www.hackerrank.com/challenges/extra-long-factorials/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys
from functools import reduce

#
# Complete the 'extraLongFactorials' function below.
#
# The function accepts INTEGER n as parameter.
#

def extraLongFactorials(n):
    print(reduce(lambda acc, val: acc * val, range(1, n+1), 1))
        

if __name__ == '__main__':
    n = int(input().strip())

    extraLongFactorials(n)

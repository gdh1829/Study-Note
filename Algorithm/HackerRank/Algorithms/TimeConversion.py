"""
https://www.hackerrank.com/challenges/time-conversion/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    reuslt = ''
    AM = 'AM'
    PM = 'PM'
    hour, rest = s.split(':', 1)
    
    if s.endswith(PM):
        hour = int(hour) + 12
        if hour == 24:
            hour = '12'
        result = f'{hour}:{rest.replace(PM, "")}'
    else:
        if hour == '12':
            hour = '00'
        result = f'{hour}:{rest.replace(AM, "")}'
    
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()

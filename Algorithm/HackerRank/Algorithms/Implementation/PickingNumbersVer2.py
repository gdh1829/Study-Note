"""
https://www.hackerrank.com/challenges/picking-numbers/problem

개선 풀이 ver2

아이디어)
- 배열 숫자를 오름차순 정렬
- 이중 루프로 비교하며 차가 1 이하가 될 수 있는 조합 탐색.
- 단, N*M(M=N)루프에서 첫번째 N이 다음 루프로 넘어갈때는, M의 시작점은 N루프의 시작점과 동일하게 시작한다. 
  M 루프의 시작점을 N과 동일하게 갖는 이유는 sorted되어 있으므로 이전 숫자들은 모두 비교가 되었기 때문.
- 각 N의 루프가 끝날때마다 가장 길었던 sub array를 비교 기록 후 최종적으로 가장 길었던 값을 반환. 
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
    longest_result = 0
    a.sort()
    
    for i in range(len(a)):
        current_length = 0
        
        for j in range(i, len(a)):
            # a is sorted, all of previous index numbers have been compared. so just needed to think about after-numbers.
            if abs(a[i] - a[j]) <= 1:
                current_length += 1
            else:
                # a is sorted, so no needed to do more
                break
        
        if longest_result < current_length:
            longest_result = current_length
    
    return longest_result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()

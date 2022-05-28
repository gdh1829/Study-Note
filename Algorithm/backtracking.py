"""
백트래킹
- 모든 경우의수를 확인해야할 때
    - for로는 확인 불가한 경우(깊이가 달라질 때)
        - ex. 2중 for문 등과 같이 정해진 루프의 깊이가 아니라 다이나믹한 경우.

- 시간복잡도: 백트래킹으로 재귀를 사용할때, 다른 알고리즘에 비해 시간 복잡도가 큼.
    - 중복 가능 => N^N => N = 8까지 가능
    - 중복 불가 => N! => N = 10까지 가능

백준 https://www.acmicpc.net/problem/15649

1. 아이디어
- 1 ~ N 중, 하나 선택 뒤 다음 Loop에서 중복 선택을 피하여 새로운 값 선택
- M까지 선택이 되면 출력

2. 시간복잡도
- N!

3. 자료구조
- 선택값 저장 int[]
"""

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

def back_tracking(list: list):
    global depth
    depth += 1
    
    # 종료 조건
    if len(list) == M:
        print(list)
        return
    
    if depth < M:
        for i in range(1, N+1):
            if list.count(i) == 0:
                list.append(i)
                back_tracking(list)
                list.pop()

depth = 0
for i in range(1, N+1):
    # 초기화
    depth = 0
    list = []
    
    list.append(i)
    back_tracking(list)

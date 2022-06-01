"""
백트래킹
- 모든 경우의수를 확인해야할 때
    - for로는 확인 불가한 경우(깊이가 달라질 때)
        - ex. 2중 for문 등과 같이 정해진 루프의 깊이가 아니라 다이나믹한 경우.

- 시간복잡도: 백트래킹으로 재귀를 사용할때, 다른 알고리즘에 비해 시간 복잡도가 큼.
    - 중복 가능 => N^N => N = 8까지 가능
    - 중복 불가 => N! => N = 10까지 가능
    - Tip 코테에서 백트래킹 문제는 N이 작음. 10 언저리. 간접적 힌트

- 재귀 함수를 사용할 때, 종료 시점 잊지말기!!

백준 https://www.acmicpc.net/problem/15649

1. 아이디어
- 1 ~ N 중, 하나 선택 뒤 다음 Loop에서 중복 선택을 피하여 새로운 값 선택
- M까지 선택이 되면 출력

2. 시간복잡도
- N!

3. 자료구조
- 방문 체크 bool[]
- 선택값 저장 int[]
"""

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
# 중복 불가 확인을 위한 숫자 사용 체크
# 문제가 자연수 1부터 시작이므로 편의상 N + 1
visited = [False] * (N + 1)
result = []

def back_tracking(num: int):
    # 재귀 종료 조건
    if num == M:
        print(" ".join(map(str, result)))
        return

    for i in range(1, N+1):    
        if not visited[i]:
            # 숫자 사용 기록
            visited[i] = True
            # 결과 추가
            result.append(i)
            # 백트래킹 재귀
            back_tracking(num + 1)
            # 재귀 완료 후 그 다음 경로 단계 복귀를 위한 방문 취소 처리
            visited[i] = False
            # 방문 복귀를 하므로 결과값 뒤로부터 제거
            result.pop()

back_tracking(0)
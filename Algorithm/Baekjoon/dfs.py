"""
백준 https://www.acmicpc.net/problem/2667

1. 아이디어
- 2중 For -> 값 1 && 방문 X -> DFS
- DFS 돌면서 찾은 값 저장 후 정렬 출력

2. 시간복잡도
- DFS: O(V+E)
- Vertex: N^2 (N 최대 25까지)
- Edge: 4N^2
- V + E: 5N^2 ~= N^2 ~= 625

3. 자료구조
- 그래프 전체 지도: int[][]
- 방문: bool[][]
- 결과값: int[]
"""

import sys
input = sys.stdin.readline

n = int(input())
map = [list(map(int, input().strip())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
yx_strategies = [(0,1), (-1,0), (0, -1), (1, 0)]
result = []
each = 0

def dfs_by_recursive(y, x):
    global each
    each += 1
    
    # 주변 그래프 탐색
    for s in yx_strategies:
        next_y = y + s[1]
        next_x = x + s[0]
        
        if 0 <= next_y < n and 0 <= next_x < n:
            if map[next_y][next_x] == 1 and not visited[next_y][next_x]:
                visited[next_y][next_x] = True
                dfs_by_recursive(next_y, next_x)

for j in range(n):
    for i in range(n):
        
        if map[j][i] == 1 and not visited[j][i]:
            # 방문 체크
            visited[j][i] = True
            # 크기 초기화
            each = 0
            # DFS 크기 구하기
            dfs_by_recursive(j, i)
            # 크기를 결과 리스트에 넣기
            result.append(each)

result.sort()
print(len(result))
for e in result:
    print(e)

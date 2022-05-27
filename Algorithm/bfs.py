"""
백준 https://www.acmicpc.net/problem/1926

1. 아이디어
- 2중 For -> 값 1 && 방문 X -> BFS
- BFS 돌면서 그림 개수 + 1, 최대값 갱신

2. 시간복잡도
- BFS: O(V+E)
- Vertex: 500 * 500
- Edge: 4 * 500 * 500
- V + E: 5 * 250000 = 1,250,000

3. 자료구조
- 그래프 전체 지도: int[][]
- 방문: bool[][]
- Queue(BFS)
"""

from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]
chk = [[False] * m for _ in range(n)]

# 오른쪽, 위쪽, 왼쪽, 아래쪽 
dy = [0,1,0,-1]
dx = [1,0,-1,0]

def bfs(y, x):
    rs = 1
    q = deque()
    q.append((y, x))
    while q:
        ey, ex = q.popleft()
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            
            # 지도 사이즈를 넘어가지 않는지 확인
            if 0 <= ny < n and 0 <= nx < m:
                # 지도가 1이고 방문하지 않은 경우
                if map[ny][nx] == 1 and chk[ny][nx] == False:
                    rs += 1
                    chk[ny][nx] = True
                    q.append((ny,nx))
    return rs

cnt = 0
maxv = 0
for j in range(n):
    for i in range(m):
        if map[j][i] == 1 and chk[j][i] == False:
            # 방문
            chk[j][i] = True
            # 전체 그림 갯수 + 1
            cnt += 1
            # BFS > 그림 크기 구하기
            maxv = max(maxv, bfs(j, i))

print(cnt)
print(maxv)

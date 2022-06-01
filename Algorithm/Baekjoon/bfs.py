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

# 맵 사이즈 입력 받기(세로크기, 가로크기)
n,m = map(int, input().split())
# 맵 만들기
map = [list(map(int, input().split())) for _ in range(n)]
# 맵 방문 기록
chk = [[False] * m for _ in range(n)]

# 4방향 진행경로 
dy = [0,1,0,-1]
dx = [1,0,-1,0]

# 너비 탐색
def bfs(y, x):
    size = 1
    # deque 컬렉션을 사용하여 속도 이점 챙기기. 맨앞뒤의 빈번한 in/out이 있을 경우, 서치 O(1)로 (리스트보다) 가장 빠름.
    dq = deque()
    # Queue 자료구조에 현재 좌표 등록.
    dq.append((y, x))
    while dq:
        # 큐의 선입된 좌표를 꺼내 4방향 진출 전략 실시.
        ey, ex = dq.popleft()
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            
            # 지도 사이즈를 넘어가지 않는지 확인.
            if 0 <= ny < n and 0 <= nx < m:
                # 지도가 1이고 방문하지 않은 경우.
                if map[ny][nx] == 1 and chk[ny][nx] == False:
                    size += 1
                    chk[ny][nx] = True
                    # 다음 너비 탐색 진출 예정지 Queue 등록
                    dq.append((ny,nx))
    return size

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

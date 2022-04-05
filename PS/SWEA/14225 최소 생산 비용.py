
from collections import deque
INF = int(1e9)

dir = [[0,1],[0,-1],[1,0],[-1,0]]
def solution(x, y):
    q = deque()
    q.append((x, y))
    distance[y][x] = 0
    while q:
        x, y = q.popleft()
        for d in dir:
            nx, ny = x+d[0], y+d[1]
            if nx<0 or ny<0 or nx>=N or ny>=N:
                continue
            cost = 1
            if height[ny][nx] > height[y][x]:
                cost += height[ny][nx] - height[y][x]
            if distance[ny][nx] > distance[y][x] + cost:
                q.append((nx, ny))
                distance[ny][nx] = distance[y][x] + cost


T = int(input())
for t in range(T):
    N = int(input())
    height = [list(map(int, input().split())) for _ in range(N)]
    distance = [[INF]*N for _ in range(N)]
    solution(0,0)
    result = distance[N-1][N-1]
    print(f'#{t+1} {result}')

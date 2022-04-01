#dijkstra

import heapq
INF = 1e9
dir = [[0,1],[0,-1],[1,0],[-1,0]]

def solution(si, sj):
    q = []
    heapq.heappush(q, (0, si, sj))
    distance[si][sj] = 0

    while q:
        dist, x, y = heapq.heappop(q)
        for d in dir:
            nx = x + d[0]
            ny = y + d[1]
            if nx<0 or ny<0 or nx>=N or ny>=N:
                continue
            if distance[nx][ny] <= dist + maps[nx][ny]:
                continue
            distance[nx][ny] = dist + maps[nx][ny]
            heapq.heappush(q, (distance[nx][ny], nx, ny))
            if nx == N-1 and ny == N-1:
                return


T = int(input())
for t in range(T):
    N = int(input())
    maps = [list(map(int, input())) for _ in range(N)]
    distance = [[INF]*N for _ in range(N)]
    solution(0, 0)
    result = distance[N-1][N-1]
    print(f'#{t+1} {result}')
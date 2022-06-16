from copy import deepcopy
from collections import deque

dir = [[0,1],[0,-1],[1,0],[-1,0]]
def solution():
    global answer
    tmpmap = deepcopy(maps)
    virus = deepcopy(viruslst)
    while virus:
        y, x = virus.popleft()
        for d in dir:
            ny, nx = y + d[0], x + d[1]
            if nx<0 or ny<0 or nx>=M or ny>=N or tmpmap[ny][nx]:
                continue
            tmpmap[ny][nx] = 2
            virus.append((ny,nx))

    safe = 0
    for row in tmpmap:
        safe += row.count(0)
    answer = max(answer, safe)

def wall(now, cnt):
    if cnt == 3:
        solution()
        return
    for idx in range(now, N*M):
        r = idx // M
        c = idx % M
        if maps[r][c] == 0:
            maps[r][c] = 1
            wall(now, cnt+1)
            maps[r][c] = 0

N, M = map(int, input().split())
maps = []
viruslst = deque()
answer = 0
for n in range(N):
    tmp = list(map(int, input().split()))
    maps.append(tmp)
    for m in range(M):
        if maps[n][m] == 2:
            viruslst.append((n, m))
wall(0, 0)

print(answer)
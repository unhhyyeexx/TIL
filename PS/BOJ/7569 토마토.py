#1:ripe 0:unripe -1:vacant
from collections import deque

delta = [[0,0,1],[0,0,-1],[0,1,0],[0,-1,0],[1,0,0],[-1,0,0]]
def solution():
    q = deque()
    for r in ripe:
        q.append(r)
    while q:
        h, i, j = q.popleft()
        for d in delta:
            nh, ni, nj = h+d[0], i+d[1], j+d[2]
            if 0<=nh<H and 0<=ni<N and 0<=nj<M and maps[nh][ni][nj]==0:
                maps[nh][ni][nj] = maps[h][i][j] + 1
                q.append([nh, ni, nj])

    result = 0
    for face in maps:
        for line in face:
            if 0 in line:
                return -1
            else:
                result = max(result, max(line))

    if result == 0:
        return 0
    return result-1

M, N, H = map(int, input().split())
maps = []
ripe = []
for h in range(H):
    one = []
    for n in range(N):
        tmp = list(map(int, input().split()))
        one.append(tmp)
        if 1 in tmp:
            for m in range(M):
                if tmp[m] == 1:
                    ripe.append([h, n, m])
    maps.append(one)

answer = solution()
print(answer)


from collections import deque

def bfs(s, path):
    queue = deque()
    for ss in s:
        queue.append(ss)

    dir = [[0,-1],[0,1],[-1,0],[1,0]]

    while queue:
        now = queue.popleft()

        for d in dir:
            nx, ny = now[0] + d[0], now[1] + d[1]

            if 0<=nx<M and 0<=ny<N and path[ny][nx]==0:
                path[ny][nx] = path[now[1]][now[0]] + 1
                queue.append([nx, ny])

    result = 0

    for p in path:
        if 0 in p: return -1
        else : result = max(result, max(p))

    if result == 0:
        return 0
    return result-1


M, N = map(int, input().split())
tomato = []
S = []
for i in range(N):
    tmp = list(map(int, input().split()))
    if 1 in tmp:
        for j in range(M):
            if tmp[j] == 1:
                S.append([j,i])
    tomato.append(tmp)

print(bfs(S, tomato))


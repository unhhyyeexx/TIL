from collections import deque

def bfs(s, g, path):
    path[s[1]][s[0]] = 1

    queue = deque()
    queue.append(s)

    dir = [[0,-1],[0,1],[-1,0],[1,0]] #상하좌우

    while queue:
        now = queue.popleft()

        for d in dir:
            nx = now[0] + d[0]
            ny = now[1] + d[1]

            if nx < 0 or ny <0 or nx >= N or ny >= N or maps[ny][nx] != 0:
                continue

            maps[ny][nx] = maps[now[1]][now[0]] + 1
            queue.append([nx, ny])

    if maps[g[1]][g[0]] == 0:
        return 0

    return maps[g[1]][g[0]]-2



T = int(input())
for t in range(T):
    N = int(input())
    maps = []
    for i in range(N):
        tmp = list(map(int, input()))
        for j in range(N):
            if tmp[j] == 1:
                tmp[j] = -1
            elif tmp[j] == 2:
                tmp[j] = 0
                S = [j,i]
            elif tmp[j] == 3:
                tmp[j] = 0
                G = [j,i]
        maps.append(tmp)

    print(f'#{t+1} {bfs(S,G,maps)}')

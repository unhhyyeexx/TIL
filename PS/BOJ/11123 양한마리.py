from collections import deque

dir = [[0,-1],[0,1],[-1,0],[1,0]]
def bfs(s):
    q = deque()
    q.append(s)

    while q:
        now = q.popleft()
        for d in dir:
            nx = now[0] + d[0]
            ny = now[1] + d[1]
            if nx<0 or ny<0 or nx>=W or ny>=H or maps[ny][nx]:
                continue
            maps[ny][nx] = 1
            q.append([nx, ny])


T = int(input())
for t in range(T):
    H, W = map(int, input().split())
    maps = []
    for _ in range(H):
        a = input()
        tmp = []
        for w in range(W):
            tmp.append(0 if a[w] == '#' else 1)
        maps.append(tmp)
    cnt = 0
    for h in range(H):
        for w in range(W):
            if maps[h][w]:
                continue
            maps[h][w] = 1
            bfs([w,h])
            cnt += 1
    print(cnt)
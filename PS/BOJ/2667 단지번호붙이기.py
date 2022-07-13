from collections import deque

dir = [[0,-1],[0,1],[-1,0],[1,0]]
def bfs(s):
    queue = deque()
    queue.append(s)

    house = 1
    while queue:
        now = queue.popleft()
        for d in dir:
            nx = now[0] + d[0]
            ny = now[1] + d[1]
            if nx<0 or ny<0 or nx>=N or ny>=N or maps[ny][nx]==0:
                continue
            maps[ny][nx] = 0
            queue.append([nx, ny])
            house += 1
    return house

N = int(input())
maps = [list(map(int, input())) for _ in range(N)]
cnt = 0
houses = []
for i in range(N):
    for j in range(N):
        if maps[i][j] == 0:
            continue
        maps[i][j] = 0
        houses.append(bfs([j,i]))
houses.sort()
print(len(houses))
print(*houses, sep='\n')
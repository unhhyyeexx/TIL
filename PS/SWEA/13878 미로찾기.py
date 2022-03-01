dir = [[0,1], [0,-1], [1,0], [-1,0]]

def dfs(y, x):
    global answer

    if answer:
        return
    for d in range(4):
        ny, nx = y+dir[d][0], x+dir[d][1]
        if ny<0 or ny>=N or nx<0 or nx>=N or maps[ny][nx] == 1:
            continue
        if maps[ny][nx] == 3:
            answer = 1
            return
        maps[y][x] = 1
        dfs(ny, nx)
        maps[y][x] = 0

T = int(input())
for t in range(T):
    N = int(input())
    maps = [list(map(int, input())) for _ in range(N)]
    graph = [0]
    x, y = 0, 0
    for i in range(N):
        for j in range(N):
            if maps[i][j] == 2:
                y, x = i, j
    answer = 0
    dfs(y, x)
    print(f'#{t+1} {answer}')
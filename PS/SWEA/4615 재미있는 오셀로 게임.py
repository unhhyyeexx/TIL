
#상하좌우, 시계방향대각선
dir = [[0,-1],[0,1],[-1,0],[1,0],[1,-1],[1,1],[-1,1],[-1,-1]]

def start(n):
    board[n//2][n//2 + 1] = 1
    board[n//2 + 1][n//2] = 1
    board[n//2 + 1][n//2 + 1] = 2
    board[n//2][n//2] = 2


def game(piece):
    x, y, color = piece[0], piece[1], piece[2]
    board[y][x] = color
    for dx, dy in dir:
        nx = x + dx
        ny = y + dy
        if nx<=0 or ny<=0 or nx>N or ny>N or board[ny][nx]==0 or board[ny][nx]==color:
            continue
        change = [[nx, ny]]
        for i in range(1, N):
            nnx = nx + (dx*i)
            nny = ny + (dy*i)
            if nnx<=0 or nny<=0 or nnx>N or nny>N or board[nny][nnx]==0:
                break
            if board[nny][nnx] == color:
                for c in change:
                    board[c[1]][c[0]] = color
                break
            else:
                change.append([nnx, nny])


T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    board = [[0] * (N+1) for _ in range(N+1)]
    start(N)
    # x, y, w/b(1:b 2:w)
    pieces = [list(map(int, input().split())) for _ in range(M)]
    for m in range(M):
        game(pieces[m])
    b, w = 0, 0
    for bb in board:
        b += bb.count(1)
        w += bb.count(2)
    print(f'#{t+1} {b} {w}')

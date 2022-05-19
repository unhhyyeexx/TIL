import sys

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
maps = [[0 for _ in range(N)] for _ in  range(N)]

for k in range(K): #mark apple
    r,c = map(int, sys.stdin.readline().split())
    maps[r-1][c-1] = 2

L = int(sys.stdin.readline())
change = dict()
for l in range(L):
    t, d = sys.stdin.readline().split()
    change[int(t)] = d

maps[0][0] = 1
#R,D,L,U
dm = [(1,0),(0,1),(-1,0),(0,-1)]

time = 0
x, y = 0, 0
move = 0
now = [(0,0)]
while True:
    time += 1
    dx, dy = dm[move]
    nx, ny = x+dx, y+dy
    #on board
    if 0<=nx<N and 0<=ny<N:
        #find apple
        if maps[ny][nx] == 2:
            now.append((nx,ny))
            maps[ny][nx] = 1
        #blank
        elif maps[ny][nx] == 0:
            maps[ny][nx] = 1
            now.append((nx,ny))
            rx, ry = now[0]
            del now[0]
            maps[ry][rx] = 0
        #bump self
        elif maps[ny][nx] == 1:
            break
        x, y = nx, ny
        #time of change direction
        if time in change:
            if change[time] == 'L':
                move -= 1
                if move >= 4:
                    move -= 4
                elif move < 0:
                    move += 4
            elif change[time] == 'D':
                move += 1
                if move >= 4:
                    move -= 4
                elif move < 0:
                    move += 4
    #out of board
    else:
        break
print(time)
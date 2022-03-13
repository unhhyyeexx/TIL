#d : 0북 1동 2남 3서
#N:세로 M:가로
#r:북쪽으로부터 떨어진 칸의 개수
#c:서쪽으로부터 떨어진 칸의 개수
#현재위치 현재방향 기준 왼쪽부터 탐색
#청소 안했으면 거기로 이동 다시 왼쪽 탐색
#왼쪽에 없으면 한 번 더 왼쪽으로 회전
#네 방향 모두 청소 되어있거나 벽이면 바라보는 방향 유지 한 칸 후진 왼쪽 탐색
#네 방향 청소 완료 벽이라 후진하려고 하는데 후진 못하면 작동 stop


# 인덱스 기준 직진 방향
dir = [[0,-1],[1,0],[0,1],[-1,0]]
clean = 0
def robot(c,r,d):
    global clean
    maps[r][c] = 1
    clean += 1
    for i in range(4):
        nd = (d+3)%4
        nc = c + dir[nd][0]
        nr = r + dir[nd][1]
        if maps[nr][nc]==0:
            robot(nc, nr, nd)
            return
        d = nd
    #후진
    bd = (d+2)%4
    bc = c + dir[bd][0]
    br = r + dir[bd][1]
    if maps[br][bc]:
        return
    else:
        robot(bc, br, d)


N, M = map(int, input().split())
R, C, D = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
robot(C, R, D)
print(clean)




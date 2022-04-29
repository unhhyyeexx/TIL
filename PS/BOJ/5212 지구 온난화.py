# X:ground .:ocean
from copy import deepcopy
delta = [[0,1],[0,-1],[1,0],[-1,0]]

def solution():
    origin = deepcopy(maps)
    # 3칸이상 바다에 접하면 잠긴다
    for i in range(R):
        for j in range(C):
            if origin[i][j] == 'X':
                check = 0
                for d in delta:
                    ni, nj = i+d[0], j+d[1]
                    if 0<=ni<R and 0<=nj<C and origin[ni][nj] == 'X':
                        check += 1
                if check <= 1:
                    maps[i][j] = '.'
    # 현재지도 구하기
    ground_r = []
    ground_c = []
    for i in range(R):
        for j in range(C):
            if maps[i][j] == '.':
                continue
            ground_r.append(i)
            ground_c.append(j)
    newmaps = []
    for i in range(min(ground_r), max(ground_r)+1):
        newmaps.append(maps[i][min(ground_c):max(ground_c)+1])
    return newmaps

R, C = map(int, input().split())
maps = [list(input()) for _ in range(R)]
result = solution()

for n in range(len(result)):
    answer = ''
    for m in range(len(result[n])):
        answer += result[n][m]
    print(answer)

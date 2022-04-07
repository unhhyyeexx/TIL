
scores  = {0:0, 1:1, 2:10, 3:100, 4:1000}
dir = [[0,1],[0,-1],[1,0],[-1,0]]
def arrange(tmp):
    student, like = tmp[0], tmp[1:]
    able = []
    for i in range(N):
        for j in range(N):
            if maps[i][j]:
                continue
            one, two = 0, 0
            for d in dir:
                ni, nj = i+d[0], j+d[1]
                if ni<0 or nj<0 or ni>=N or nj>=N:
                    continue
                if maps[ni][nj] in like:
                    one += 1
                if not maps[ni][nj]:
                    two += 1
            able.append((one, two, i, j))
    able.sort(key = lambda x : (-x[0], -x[1], x[2], x[3]))
    fi, fj = able[0][2], able[0][3]
    maps[fi][fj] = student


def evaluate(i, j):
    global satisfaction
    student = maps[i][j]
    like = lst[student-1][1:]
    score = 0
    for d in dir:
        ni, nj = i+d[0], j+d[1]
        if ni<0 or nj<0 or ni>=N or nj>=N or maps[ni][nj] not in like:
            continue
        score += 1
    satisfaction += scores[score]


N = int(input())
maps = [[0]*N for _ in range(N)]
lst = [list(map(int, input().split())) for _ in range(N*N)]
satisfaction = 0

for n in range(N*N):
    arrange(lst[n])

lst.sort(key = lambda x : x[0])
for i in range(N):
    for j in range(N):
        evaluate(i, j)

print(satisfaction)

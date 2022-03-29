
dir = [[1,0],[0,1]]
def solution(i, j, sumvalue):
    global answer
    if sumvalue >= answer:
        return
    if i==N-1 and j==N-1:
        answer = min(sumvalue, answer)
        return
    for d in dir:
        nx = i + d[0]
        ny = j + d[1]
        if nx<0 or ny<0 or nx>=N or ny>=N :
            continue
        sumvalue += maps[nx][ny]
        solution(nx, ny, sumvalue)
        sumvalue -= maps[nx][ny]


T = int(input())
for t in range(T):
    N = int(input())
    maps = [list(map(int, input().split())) for _ in range(N)]
    answer = 1e9
    solution(0, 0, maps[0][0])
    print(f'#{t+1} {answer}')

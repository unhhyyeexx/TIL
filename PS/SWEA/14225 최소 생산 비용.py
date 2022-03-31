
def solution(now, sumvalue):
    global answer
    if answer <= sumvalue:
        return
    if now == N:
        answer = min(answer, sumvalue)
        return
    for n in range(N):
        if not visit[n]:
            visit[n] = 1
            new_sumvalue = sumvalue + maps[now][n]
            solution(now +1, new_sumvalue)
            visit[n] = 0

T = int(input())
for t in range(T):
    N = int(input())
    maps = [list(map(int, input().split())) for _ in range(N)]
    visit = [0] * N
    answer = 1e9
    solution(0,0)
    print(f'#{t+1} {answer}')
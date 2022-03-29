
def solution(now, sumvalue, cnt):
    global answer

    if cnt == N:
        sumvalue += maps[now][0]
        answer = min(answer, sumvalue)
        return
    if answer <= sumvalue:
        return
    for i in range(1, N):
        if i == now or visit[i]:
            continue
        visit[i] = 1
        solution(i, sumvalue+maps[now][i], cnt+1)
        visit[i] = 0


T = int(input())
for t in range(T):
    N = int(input())
    maps = [list(map(int, input().split())) for _ in range(N)]
    visit = [0] * N
    answer = 1e9
    solution(0, 0, 1)

    print(f'#{t+1} {answer}')


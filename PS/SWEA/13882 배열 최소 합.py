def dfs(d, sumvalue):
    global answer
    if sumvalue >= answer:
        return
    if d == N:
        answer = min(answer, sumvalue)
        return
    for i in range(N):
        if visit[i]:
            continue

        visit[i] = 1
        sumvalue += lst[d][i]
        dfs(d+1, sumvalue)
        visit[i]=0
        sumvalue -= lst[d][i]


T = int(input())
for t in range(T):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    visit = [0]*N
    answer = 10*10
    dfs(0,0)
    print(f'#{t+1} {answer}')

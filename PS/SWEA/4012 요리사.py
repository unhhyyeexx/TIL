
def f(n, idx):
    global answer



    for i in range(idx+1, N):
        if visit[i]:
            continue
        visit[i] = 1
        f(n, i)



T = int(input())
for t in range(T):
    N = int(input())
    info = [list(map(int, input().split())) for _ in range(N)]
    visit = [0]*N
    answer = 1e9



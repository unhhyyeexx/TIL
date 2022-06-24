#dp

N = int(input())
maps = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*N for _ in range(N)]

dp[0][0] = 1
for i in range(N):
    for j in range(N):
        dist = maps[i][j]
        if dist == 0 or dp[i][j] == 0:
            continue
        ni, nj = i+dist, j+dist
        if ni < N :
            dp[ni][j] += dp[i][j]
        if nj < N :
            dp[i][nj] += dp[i][j]

answer = dp[N-1][N-1]
print(answer)
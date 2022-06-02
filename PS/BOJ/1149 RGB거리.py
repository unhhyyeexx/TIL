
N = int(input())
cost = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*3 for _ in range(N)]

for i in range(N):
    for j in range(3):
        if i == 0:
            dp[i][j] = cost[i][j]
        else:
            dp[i][j] = min(dp[i-1][(j+1)%3], dp[i-1][(j+2)%3]) + cost[i][j]
print(min(dp[-1]))

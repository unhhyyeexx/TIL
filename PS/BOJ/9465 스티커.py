
T = int(input())
for t in range(T):
    n = int(input())
    cost = [list(map(int, input().split())) for _ in range(2)]

    dp = [[0]*n for _ in range(2)]

    dp[0][0] = cost[0][0]
    dp[1][0] = cost[1][0]

    for i in range(1, n):
        if i == 1:
            dp[0][1] = cost[1][0] + cost[0][1]
            dp[1][1] = cost[0][0] + cost[1][1]
        else:
            dp[0][i] = cost[0][i] + max(dp[1][i-2], dp[1][i-1])
            dp[1][i] = cost[1][i] + max(dp[0][i-2], dp[0][i-1])
    print(max(dp[0][n-1], dp[1][n-1]))

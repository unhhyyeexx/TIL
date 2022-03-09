
n = int(input())

dp = [0]*(n+1) #최소값
path = [[] for _ in range(n+1)] #최소경로
path[1].append(1)

for i in range(2, n+1):
    dp[i] = dp[i-1] + 1
    path[i] = path[i-1] + [i]

    if i % 3 == 0 and dp[i//3]+1 < dp[i]:
        dp[i] = dp[i//3]+1
        path[i] = path[i//3] + [i]
    if i % 2 == 0 and dp[i//2]+1 < dp[i]:
        dp[i] = dp[i//2]+1
        path[i] = path[i//2] + [i]

print(dp[-1])
print(*reversed(path[-1]))
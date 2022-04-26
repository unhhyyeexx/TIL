
INF = int(1e9)
C, N = map(int, input().split())
dp = [0] + [INF]*(C+100)

arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort()

for w, v in arr:
    for idx in range(v, C+101):
        dp[idx] = min(dp[idx-v]+w, dp[idx])

print(min(dp[C:]))

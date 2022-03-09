
def jump(n, path):
    dp = [n] *n
    dp[0] = 0
    for i in range(n):
        for j in range(1, path[i] + 1):
            if i + j >= n:
                break
            dp[i + j] = min(dp[i + j], dp[i] + 1)

    if dp[-1] != n:
        return dp[-1]
    return -1


N = int(input())
lst = list(map(int, input().split()))
print(jump(N, lst))



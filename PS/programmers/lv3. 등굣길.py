
def solution(m, n, puddles):
    dp = [[0]*(m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i==1 and j == 1:
                dp[1][1] = 1
            elif [j, i] not in puddles:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    answer = dp[n][m] % 1000000007
    return answer

muzi = 4
neo = 3
appeach = [[2,2]]

frodo = solution(muzi, neo, appeach)
print(frodo)
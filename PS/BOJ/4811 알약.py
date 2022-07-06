
import sys
input = sys.stdin.readline


# n의 최대값 30
# dp[i][j]에서 i는 whole개수 j는 half개수
# 즉, dp[i][j]는 whole i개, half j개로 만들 수 있는 경우의 수
dp = [[0]*31 for _ in range(31)]

# whole이 없고 half만 있을 경우 경우의 수는 half를 선택하는 것 하나뿐
for half in range(1,31):
    dp[0][half] = 1

for i in range(1, 31):
    for j in range(30):
        # 남은 half가 없으면 무조건 whole 선택 => half가 무조건 한 개 생김
        if j == 0:
            dp[i][j] = dp[i-1][j+1]
        # 남은 half가 있으면 whole을 선택하는 경우와, half를 선택하는 경우를 둘 다 고려해서 더해줌
        else:
            dp[i][j] = dp[i-1][j+1] + dp[i][j-1]

while True:
    n = int(input())
    if n == 0:
        break
    print(dp[n][0])
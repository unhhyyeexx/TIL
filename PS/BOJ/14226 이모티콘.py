import sys
from collections import deque

input = sys.stdin.readline


def solution(s):
    global answer
    # s의 최대값 1001
    # dp[i][j] = x ;
    # 화면에 보이는 이모티콘 개수 i개;
    # 클립보드에 복사되어 있는 이모티콘 개수 j개;
    # 걸린 시간 x
    dp = [[-1] * 1001 for _ in range(1001)]
    dp[1][0] = 0
    q = deque([[1, 0]])

    while q:
        i, j = q.popleft()
        # 1. 화면에 있는 i개의 이모티콘을 복사해서 클립보드에 저장하는 경우
        if i <= 1000:
            if dp[i][i] == -1:
                dp[i][i] = dp[i][j] + 1
                q.append([i, i])

        # 2. 클립보드에 있는 j개의 이모티콘을 화면에 붙여넣기 하는 경우
        if i + j <= 1000:
            if dp[i+j][j] == -1:
                dp[i+j][j] = dp[i][j] + 1
                q.append([i+j, j])

        # 3. 화면에 있는 이모티콘 중 하나를 삭제하는 경우
        if i - 1 >= 0:
            if dp[i-1][j] == -1:
                dp[i-1][j] = dp[i][j] + 1
                q.append([i-1, j])

        # 화면의 이모티콘이 s개이면 stop
        if i == s:
            break

    for col in dp[s]:
        if col != -1:
            answer = min(answer, col)

    return answer


string = int(input())
answer = int(1e9)

print(solution(string))
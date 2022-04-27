def solution(board, skill):
    answer = 0
    N, M = len(board), len(board[0])
    arr = [[0] * (M + 1) for _ in range(N + 1)]
    for type, r1, c1, r2, c2, degree in skill:
        arr[r1][c1] += degree * (-1 if type == 1 else 1)
        arr[r1][c2 + 1] += degree * (1 if type == 1 else -1)
        arr[r2 + 1][c1] += degree * (1 if type == 1 else -1)
        arr[r2+1][c2+1] += degree * (-1 if type == 1 else 1)

    for i in range(N):
        for j in range(M):
            arr[i][j + 1] += arr[i][j]

    for j in range(M):
        for i in range(N):
            arr[i + 1][j] += arr[i][j]

    for i in range(N):
        for j in range(M):
            if board[i][j] + arr[i][j] > 0:
                answer += 1

    return answer

frodo = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
muzi = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]
appeach = solution(frodo, muzi)
print(appeach)
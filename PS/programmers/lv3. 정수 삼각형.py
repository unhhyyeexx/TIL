
def solution(triangle):
    N = len(triangle)
    for i in range(1, N):
        for j in range(i+1):
            if j == 0:
                triangle[i][j] += triangle[i-1][j]
            elif j == i:
                triangle[i][j] += triangle[i-1][j-1]
            else:
                maxv = max(triangle[i-1][j], triangle[i-1][j-1])
                triangle[i][j] += maxv
    answer = max(triangle[-1])
    return answer

frodo = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
muzi = solution(frodo)
print(muzi)

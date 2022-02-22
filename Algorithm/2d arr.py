# #지그재그 순회
# for i in range(n): #행
#     for j in range(m):
#         arr[i][j + (m-1-2*j)*(i%2)]


#practice 1
n = 3
arr = [[1,2,3],[4,5,6],[7,8,9]]
# arr = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
# arr = [list(map(int, input().split())) for _ in range(5)]
for i in range(n):
    arr[i] = [arr[i][0]] + arr[i] + [arr[i][-1]]
arr = [arr[0]] + arr + [arr[-1]]
dx = [0,0,-1,1]#하 상 좌 우
dy = [1,-1,0,0]
total = 0
for i in range(1,n+1):
    for j in range(1,n+1):
        one = 0
        for k in range(4):
            nx, ny = j+dx[k], i+dy[k]
            one += arr[i][j] - arr[ny][nx]  if arr[i][j] - arr[ny][nx]> 0 else arr[ny][nx] - arr[i][j]
        total += one
print(total)
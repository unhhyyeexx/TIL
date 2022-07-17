

h, w = map(int, input().split())
height = list(map(int, input().split()))
maps = [[0]*h for _ in range(w)]
for i in range(w):
    for j in range(height[i]):
        maps[i][j] = 1


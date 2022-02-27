#1. 주어진 리스트 중에서 최소값을 찾는다
#2. 그 값을 리스트의 맨 앞에 위치한 값고 교환한다.
#3. 맨 처음 위치를 제외한 나머지 리스트를 대상으로 과정 반복
#
# def selection_sort(arr):
#     n = len(arr)
#     for i in range(n-1):
#         minidx = i
#         for j in range(i+1, n):
#             if arr[minidx] > arr[j]:
#                 minidx = j
#         arr[i], arr[minidx] = arr[minidx], arr[i]

#practice 3
five = [[9,20,2,18,11],[19,1,25,3,21],[8,24,10,17,7],[15,4,16,5,6],[12,13,22,23,14]]

def selection(arr):
    n = len(arr)
    for i in range(n-1):
        minidx = i
        for j in range(i+1, n):
            if arr[minidx] > arr[j]:
                minidx = j
        arr[minidx],arr[i] = arr[i], arr[minidx]
    return arr

def fivesnail(arr):
    snaillst = [[0]*5 for _ in range(5)]
    dx = [1,0,-1,0]#우 하 좌 상
    dy = [0,1,0,-1]
    idx = 0
    x, y, dir = 0, 0, 0
    while idx < len(arr):
        snaillst[y][x] = arr[idx]
        nx = x+dx[dir]
        ny = y+dy[dir]
        if nx <0 or ny < 0 or nx >= 5 or ny >= 5 or snaillst[ny][nx]!=0:
            dir = (dir+1)%4
            nx = x + dx[dir]
            ny = y + dy[dir]
        x, y = nx, ny
        idx += 1
    return snaillst


lst = []
for i in range(5):
    for j in range(5):
        lst += [five[i][j]]

sortarr = selection(lst)
result = fivesnail(sortarr)
print(result)





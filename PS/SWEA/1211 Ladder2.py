dx = [0,0,-1]
dy = [1,-1,0]
c = 100
for case in range(10):
    n = int(input())
    arrorigin = []
    for t in range(c):
        arrorigin.append(list(map(int, input().split())))

    x = c-1
    y = list(filter(lambda a: arrorigin[-1][a] == 1, range(len(arrorigin[-1]))))
    mingaro = c*c
    result = 0
    for yy in y:
        x = c-1
        arr = [item[:] for item in arrorigin]
        garo = 0
        while True:
            if x == 0:
                result = yy
                mingaro = garo
                break
            else:
                for t in range(3):
                    nx = x + dx[t]
                    ny = yy + dy[t]
                    if 0 <= nx < c and 0 <= ny < c and arr[nx][ny] == 1:
                        if ny != yy:
                            garo += 1
                        arr[nx][ny] = 0
                        x, yy = nx, ny
                        break
                if garo >= mingaro:
                    break
    print(f'#{n} {result}')

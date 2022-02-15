#### SWEA 1210 Ladder1

```python
T = 10
for t in range(T):
    n = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    for i in range(100):
        ladder[i] = [0] + ladder[i] + [0]

    #2가 몇번째 column에 있을까?
    arrive = ladder[99].index(2)

    #2에서부터 경로따라 위로 올라가기
    #다른방향에 1이 생기면 방향 바꾸기
    #지나온 길은 0으로 만들고, 양옆에 1탐색 우선순위로 둔다
    dx = [1, 0, -1] #R U L
    dy = [0, -1, 0]
    x, y = arrive, 99
    dir = 1
    while y > 0:
        if ladder[y+dy[dir]][x+dx[dir]]==1:
            if ladder[y+dy[(dir-1)%3]][x+dx[(dir-1)%3]]:
                dir = (dir-1)%3
            elif ladder[y+dy[(dir+1)%3]][x+dx[(dir+1)%3]]:
                dir = (dir+1)%3
        
        ladder[y][x] = 0
        x += dx[dir]
        y += dy[dir]
        
        if x < 1 or y < 0 or x >= 101 or y >= 100 or ladder[y][x] == 0:
            x -= dx[dir]
            y -= dy[dir]
            ladder[y][x] = 1
            if ladder[y+dy[(dir-1)%3]][x+dx[(dir-1)%3]]:
                dir = (dir-1)%3
            elif ladder[y+dy[(dir+1)%3]][x+dx[(dir+1)%3]]:
                dir = (dir+1)%3

    print(f'#{n} {x-1}')
```
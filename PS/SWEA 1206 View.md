#### SWEA 1206 View

```python
T = 10

for t in range(T):
    coord = [[0 for _ in range(255)] for _ in range(1001)]
    length = int(input())
    height = list(map(int, input().split()))
    for i in range(length):
        coord[i][0:height[i]] = [1]*height[i]
    cnt = 0
    for i in range(length):
        for j in range(max(height)):
            if coord[i][j] == 1 and coord[i-2][j] == 0 and coord[i-1][j] == 0 and coord[i+1][j]==0 and coord[i+2][j] == 0:
                cnt += 1

    print(f'#{t+1} {cnt}')
```


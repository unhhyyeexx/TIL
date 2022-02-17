#### SWEA 1209 Sum

```python
for t in range(10):
    num = int(input())
    maps = [list(map(int, input().split())) for _ in range(100)]

    dia1, dia2 = 0, 0
    checklist = []
    for i in range(100):
        row = 0
        column = 0
        for j in range(100):
            row += maps[i][j]
            column += maps[j][i]
            
        checklist.append(max(row, column))
        dia1 += maps[i][i]
        dia2 += maps[i][99-i]
    
    checklist.append(max(dia1, dia2))
    
    print(f'#{num} {max(checklist)}')
```


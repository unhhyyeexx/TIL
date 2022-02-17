#### SWEA 1208 Flatten

```python
T = 10
for t in range(T):
    dump = int(input())
    lst = list(map(int, input().split()))
    cnt = 0
    sub = 0
    while cnt != dump:
        lst = sorted(lst)
        lst[0] += 1
        lst[-1] -= 1
        cnt += 1
    sub = max(lst) - min(lst)   

    print(f'#{t+1} {sub}')
```


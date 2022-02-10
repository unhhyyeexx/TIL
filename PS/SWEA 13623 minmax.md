#### SWEA 13623 minmax

```python
T = int(input())
for t in range(T):
    N = int(input())
    nums = list(map(int,input().split()))
    #bubble sort
    for n in range(N-1, 0, -1):
        for i in range(0,n):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
    print(f'#{t+1} {nums[-1]-nums[0]}')
```


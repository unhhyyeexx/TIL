#### SWEA 1208 Flatten (except min,max,sort)

```python
T = 10
#입력
for t in range(T):
    dump = int(input())
    lst = list(map(int, input().split()))
    cnt = 0
    sub = 0
    #주어진 횟수 끝나면 반복문 종료
    while cnt != dump:
        #bubble sort -> 가장 높은 곳의 위치와 낮은 곳의 위치 찾기 위해서
        for n in range(len(lst)-1, 0, -1):
            for i in range(0,n):
                if lst[i] > lst[i+1]:
                    lst[i], lst[i+1] = lst[i+1], lst[i]
        lst[0] += 1 #가장 낮은 곳 +1
        lst[-1] -= 1 #가장 높은곳 -1
        cnt += 1
    #bubble sort -> 반복문 종료 후 가장 높은 곳과 낮은 곳의 위치 차 구하기 위해
    for n in range(len(lst)-1, 0, -1):
            for i in range(0,n):
                if lst[i] > lst[i+1]:
                    lst[i], lst[i+1] = lst[i+1], lst[i]
    sub = lst[-1] - lst[0] 

    print(f'#{t+1} {sub}')
```


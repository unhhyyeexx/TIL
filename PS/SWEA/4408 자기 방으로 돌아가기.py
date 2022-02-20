T = int(input())
for t in range(T):
    path = [0 for _ in range(200)]
    N = int(input()) #학생수
    student = [list(map(int, input().split())) for _ in range(N)]
    path = [0] * 200
    for start, end in student:
        if start > end :
            start, end = end, start
        for s in range((start-1)//2 , (end-1)//2+1):
            path[s] += 1
    print(f'#{t+1} {max(path)}')


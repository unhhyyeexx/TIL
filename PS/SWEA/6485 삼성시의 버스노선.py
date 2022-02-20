T = int(input())
for t in range(T):
    station = [0] * 5000
    result = ''
    N = int(input())
    for _ in range(N):
        start, end = map(int, input().split())
        for i in range(start-1, end):
            station[i] += 1
    P = int(input())
    for _ in range(P):
        idx = int(input())
        result += str(station[idx-1])

    print(f'#{t+1} {" ".join(result)}')

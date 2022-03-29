
T = int(input())
for t in range(T):
    N = int(input())
    timetable = []
    for _ in range(N):
        timetable.append(list(map(int, input().split())))
    timetable.sort(key = lambda x : (x[1], x[0]))

    answer = end = 0
    for s, e in timetable:
        if s >= end:
            answer += 1
            end = e
    print(f'#{t+1} {answer}')
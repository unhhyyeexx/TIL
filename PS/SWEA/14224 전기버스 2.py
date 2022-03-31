
def solution(now, cnt):
    global answer
    if answer <= cnt:
        return
    if now >= N-1:
        answer = min(answer, cnt)
        return
    for n in range(battery[now]):
        solution(now+n+1, cnt+1)


T = int(input())
for t in range(T):
    tmp = list(map(int, input().split()))
    N, battery = tmp[0], tmp[1:]
    answer = 1e9
    solution(0, -1)

    print(f'#{t+1} {answer}')


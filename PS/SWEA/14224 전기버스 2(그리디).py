
def solution(now):
    global answer
    while True:
        maxvalue, nexti = 0, 0
        val = battery[now]

        if now + val >= N - 1:
            return

        for i in range(1, val+1):
            if battery[now+i] +i > maxvalue:
                maxvalue = battery[now+i] +i
                nexti = now + i
        now = nexti
        answer += 1

T = int(input())
for t in range(T):
    tmp = list(map(int, input().split()))
    N, battery = tmp[0], tmp[1:]
    answer = 0
    solution(0)
    print(f'#{t+1} {answer}')


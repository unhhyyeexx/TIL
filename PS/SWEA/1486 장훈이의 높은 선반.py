#B:선반높이 N:직원의 수
def solution(idx, sumvalue):
    global answer
    if sumvalue > answer:
        return
    if idx >= N:
        if sumvalue >= B:
            answer = sumvalue
        return
    visit[idx] = 1
    solution(idx+1, sumvalue+talllist[idx])
    visit[idx] = 0
    solution(idx+1, sumvalue)


    return


T = int(input())
for t in range(T):
    N, B =map(int, input().split())
    talllist = sorted(list(map(int, input().split())))
    visit = [0] * N
    answer = sum(talllist)
    solution(0,0)
    result = answer-B
    print(f'#{t+1} {result}')


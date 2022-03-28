
def solution(w, t):
    global answer

    while t and w:
        nt = t.pop()
        while w:
            nw = w.pop()
            if nt >= nw:
                answer += nw
                break


T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    weight = sorted(list(map(int, input().split())))
    truck = sorted(list(map(int, input().split())))
    answer = 0
    solution(weight, truck)
    print(f'#{tc+1} {answer}')

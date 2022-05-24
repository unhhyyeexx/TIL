INF = int(1e9)
def solution(start):
    global answer

    stack = [start]
    path = [start]

    while stack:
        now = stack.pop()
        next = choice[now]
        if not visit[next]:
            visit[next] = now
            stack.append(next)
            path.append(next)
        else:
            if visit[next] == -1:
                break
            if visit[next] != INF:
                while path:
                    pre = path.pop()
                    if visit[pre] != INF:
                        answer += 1
                        visit[pre] = INF
                    if pre == next:
                        break

    while path:
        p = path.pop()
        visit[p] = -1

T = int(input())
for t in range(T):
    n = int(input())
    choice = [0] + list(map(int, input().split()))
    visit = [0]*(n+1)
    answer = 0

    for i in range(1, n+1):
        if choice[i] == i:
            visit[i] = INF
            answer += 1

    for i in range(1, n+1):
        if not visit[i]:
            solution(i)

from collections import deque

def solution(s, g):
    global answer
    q = deque([(s, 1)])
    while q:
        now, d = q.popleft()
        if now == g:
            answer = d
            break
        if now*2 <= g:
            q.append((now*2, d+1))
        if now*10+1 <= g:
            q.append(((now*10+1), d+1))


a, b= map(int, input().split())
answer = -1
solution(a, b)
print(answer)


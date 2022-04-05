#bfs,,?
from collections import deque

def solution(s, g):
    q = deque()
    q.append(s)
    visit[s] = 1

    while q:
        num = q.popleft()
        if num == g:
            return
        cnt = visit[num] + 1
        if 1 <= num + 1 <= 1000000 and not visit[num+1]:
            visit[num + 1] = cnt
            q.append(num+1)
        if 1 <= num - 1 <= 1000000 and not visit[num-1]:
            visit[num - 1] = cnt
            q.append(num-1)
        if 1 <= num * 2 <= 1000000 and not visit[num*2]:
            visit[num * 2] = cnt
            q.append(num*2)
        if 1 <= num - 10 <= 1000000 and not visit[num-10]:
            visit[num - 10] = cnt
            q.append(num-10)

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    visit = [0] * 1000001
    solution(N, M)
    print(f'#{t+1} {visit[M]-1}')


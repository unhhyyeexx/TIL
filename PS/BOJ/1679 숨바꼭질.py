from collections import deque

def bfs(s, g):
    q = deque()
    q.append(s)

    while q:
        now = q.popleft()
        if now == g:
            return
        dir = [now+1, now-1, now*2]
        for new in dir:
            if new<0 or new>inf or distance[new]:
                continue
            distance[new] = distance[now] + 1
            q.append(new)


inf = 100000
N, K = map(int, input().split())
distance = [0] * (inf+1)
bfs(N, K)
print(distance[K])
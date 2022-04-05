
import heapq
INF = int(1e9)

def solution(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


T = int(input())
for t in range(T):
    N, E = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    distance  = [INF] * (N+1)

    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append((e, w))

    solution(0)
    result = distance[N]
    print(f'#{t+1} {result}')


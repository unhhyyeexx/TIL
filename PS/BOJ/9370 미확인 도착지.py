
import heapq
import sys
INF = int(1e9)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start, start))
    distance[start][0] = 0
    while q:
        dist, now, pre = heapq.heappop(q)
        if distance[now][0] < dist:
            continue
        if (now == g and pre == h) or (now == h and pre == g):
            distance[now][1] = 1
        for i in graph[now]:
            cost = dist + i[1]
            if cost <= distance[i[0]][0]:
                distance[i[0]][0] = cost
                distance[i[0]][1] = distance[now][1]
                # if (now==g and i[0]==h) or (now==h and i[0]==g):
                #     c = 1
                # if distance[i[0]][1] == 0 and c == 1:
                #     distance[i[0]][1] = c
                # elif distance[i[0]][1] == 1 and c == 0 and cost < distance[i[0]][0]:
                #     distance[i[0]][1] = c
                heapq.heappush(q, (cost, i[0], now))

T = int(input())
for tc in range(T):
    #교차로, 도로, 목적지후보개수
    n, m, t = map(int, sys.stdin.readline().split())
    #출발지, 교차로 양옆
    s, g, h = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n+1)]
    distance = [[INF, 0] for _ in range(n+1)]
    for _ in range(m):
        a, b, d = map(int, sys.stdin.readline().split())
        graph[a].append((b, d))
        graph[b].append((a, d))
    goals = list(int(input()) for _ in range(t))

    dijkstra(s)

    result = []
    for goal in goals:
        if distance[goal][1] == 1:
            result.append(goal)
    print(*sorted(result))


from collections import deque

def bfs(s, g, path):
    distance = [0]*(len(path))
    distance[s] = 1 #start point

    queue = deque()
    queue.append(s)

    while queue: #queue에 원소가 있을때만
        now = queue.popleft()
        dist = distance[now]

        for next in path[now]:
            if distance[next]:
                continue
            distance[next] = dist+1
            queue.append(next)

    if distance[g] == 0:
        return 0

    return distance[g] -1



T = int(input())
for t in range(T):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]

    for i in range(e):
        n1, n2 = map(int, input().split())
        graph[n1].append(n2)
        graph[n2].append(n1)

    S, G = map(int, input().split())

    print(f'#{t+1} {bfs(S,G,graph)}')

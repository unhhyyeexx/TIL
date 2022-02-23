
def dfs(now, goal, path):
    global answer
    if now == goal:
        answer = 1
        return

    for n in path[now]:
        if not visit[n]:
            visit[n] = 1
            dfs(n, goal, path)
            visit[n] = 0

#V개 노드 E개 간선
#n1, n2 간선 정보 (출발노드 간선노드)
#s,g 경로의 존재를 확인할 출발노드, 간선노드
T = int(input())
for t in range(T):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    for i in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)

    s, g = map(int, input().split())
    visit = [0] * (V + 1)
    answer = 0
    dfs(s, g, graph)
    print(f'#{t+1} {answer}')



from collections import deque

def bfs(s):
    visit = []
    global answer
    queue = deque()
    queue.append([s,0])
    visit.append(s)

    while queue:
        now, cnt = queue.popleft()
        if now not in graph:
            continue
        for new in graph[now]:
            if new not in visit:
                visit.append(new)
                answer.append([new, cnt+1])
                queue.append((new, cnt+1))

T = 10
for t in range(T):
    N, S = map(int, input().split())
    tmp = list(map(int, input().split()))
    graph= dict()
    for i in range(0, N, 2):
        if tmp[i] in graph and tmp[i+1] not in graph[tmp[i]]:
            graph[tmp[i]].append(tmp[i+1])
        elif tmp[i] not in graph:
            graph[tmp[i]] = [tmp[i+1]]
    answer= []
    bfs(S)
    result = sorted(answer, key=lambda x: (-x[1], -x[0]))
    print(f'#{t+1} {result[0][0]}')






# def dfs(s,cnt):
#     global answer
#     if s not in graph:
#         answer.append([s, cnt])
#         return
#     check = 0
#     for j in range(len(graph[s])):
#         if visit[graph[s][j]] == 1:
#             check += 1
#             continue
#
#         visit[graph[s][j]] = 1
#         dfs(graph[s][j], cnt+1)
#         visit[graph[s][j]] = 0
#
#     if check == len(graph[s]):
#         answer.append([s, cnt])
#         return
# T = 10
# for t in range(T):
#     N, S = map(int, input().split())
#     tmp = list(map(int, input().split()))
#     graph, visit, dist = dict(), dict(), dict()
#     for i in range(0, N, 2):
#         if tmp[i] in graph and tmp[i+1] not in graph[tmp[i]]:
#             graph[tmp[i]].append(tmp[i+1])
#         elif tmp[i] not in graph:
#             graph[tmp[i]] = [tmp[i+1]]
#         if tmp[i] not in visit: visit[tmp[i]] = 0
#         if tmp[i+1] not in visit: visit[tmp[i+1]] = 0
#         if tmp[i] not in dist: dist[tmp[i]] = 1e9
#         if tmp[i+1] not in dist: dist[tmp[i+1]] = 1e9
#
#     visit[S] = 1
#     answer = []
#     dfs(S, 0)
#     result = sorted(answer, key = lambda x:(-x[1], -x[0]))
#     print(f'#{t+1} {result[0][0]}')
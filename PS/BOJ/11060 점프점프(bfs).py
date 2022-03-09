from collections import deque

def bfs(n, lst):

    queue = deque()
    queue.append(0)
    visit = [0]*n
    visit[0] = 1

    while queue:
        idx = queue.popleft()
        for i in range(1, lst[idx]+1):
            if idx+i >= n or visit[idx+i]:
                continue
            visit[idx+i] = visit[idx]+1
            queue.append(idx+i)
    if not visit[-1]:
        return -1

    return visit[-1]-1


N = int(input())
maps = list(map(int, input().split()))
print(bfs(N, maps))



# from collections import deque
# # 메모리 초과
# def bfs(n, path):
#     if n == 1:
#         return 0
#
#     queue = deque()
#     queue.append([0,0]) #현재 인덱스, 점프cnt
#
#     while queue:
#         idx, distnce = queue.popleft()
#
#         if idx == n-1:
#             return distnce
#
#         for j in path[idx]:
#             if j >= n: break
#             queue.append([j, distnce+1])
#
#     return -1
#
#
# N = int(input())
# maps = list(map(int, input().split()))
# graph = deque()
# for i in range(N):
#     graph.append(list(range(i+1,i+maps[i]+1)))
# print(graph)
# print(bfs(N, graph))


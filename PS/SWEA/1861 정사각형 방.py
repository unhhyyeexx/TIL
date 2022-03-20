from collections import deque

dir = [[0,-1],[0,1],[-1,0],[1,0]]#상하좌우
def solution(s):
    global answer
    queue = deque()
    queue.append(s)
    dist = [[0] * N for _ in range(N)]

    while queue:
        now = queue.popleft()
        for d in dir:
            nx = now[0] + d[0]
            ny = now[1] + d[1]
            if




    return

T = int(input())
for t in range(T):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    answer = []


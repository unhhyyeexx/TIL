from collections import deque
dir = [[0,-1],[-1,0],[0,1],[1,0]]

def solution(move):
    global w, h
    x, y, i = 0, 0, 0
    move = deque(move)
    while move:
        now = move.popleft()
        if now in ['F', 'B']:
            x += dir[i][0] if now == 'F' else -dir[i][0]
            y += dir[i][1] if now == 'F' else -dir[i][1]
            if i in [0,2]:
                h.append(y)
            elif i in [1,3]:
                w.append(x)
        elif now in ['R', 'L']:
            i += 1 if now == 'L' else -1
            i %= 4

T = int(input())
for t in range(T):
    control = list(input())
    w, h = [0], [0]
    solution(control)
    width = max(w) - min(w)
    height = max(h) - min(h)
    print(width * height)

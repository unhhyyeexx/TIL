import sys

#base direction: cw
#1N 2S 3W 4E
def zero_to_there(dir, dis, width, height):
    if dir == 1: return dis
    elif dir == 2: return width + height + (width - dis)
    elif dir == 3: return width + height + width + (height - dis)
    elif dir == 4: return width + dis

w, h = map(int, sys.stdin.readline().split())
N = int(input()) #number of store

#location : (direction, distance)
#distance from 0point to store
stores = []
for n in range(N):
    direction, distance = map(int, input().split())
    stores.append(zero_to_there(direction, distance, w, h))
#dong-geun input
ddir, ddis = map(int, input().split())
dong = zero_to_there(ddir, ddis, w, h)

result = 0

#clockwise vs counterclockwise
for n in range(N):
    cw = abs(dong - stores[n])
    ccw = 2*(w+h) - cw
    result += min(cw, ccw)

print(result)



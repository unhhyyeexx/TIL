import sys

N = int(sys.stdin.readline())
time = []
for _ in range(N):
    S, E = map(int, sys.stdin.readline().split())
    time.append([S, E])

time = sorted(time, key = lambda x : (x[1],x[0]))

end = 0
cnt = 0
for s, e in time:
    if s >= end:
        cnt += 1
        end = e
print(cnt)
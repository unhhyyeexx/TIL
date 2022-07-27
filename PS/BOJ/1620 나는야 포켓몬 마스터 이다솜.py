
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
pm1, pm2 = dict(), dict()
for i in range(1, n+1):
    pm = input().rstrip()
    pm1[pm] = i
    pm2[i] = pm
for _ in range(m):
    q = input().rstrip()
    if q.isalpha():
        print(pm1[q])
    else:
        print(pm2[int(q)])


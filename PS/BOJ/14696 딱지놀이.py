import sys

N = int(sys.stdin.readline())
figure = [4, 3, 2, 1]
result = []

for _ in range(N):
    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))

    for f in figure:
        if f == 1:
            if a[1:a[0] + 1].count(f) > b[1:b[0] + 1].count(f):
                result.append('A')
                break
            elif a[1:a[0] + 1].count(f) < b[1:b[0] + 1].count(f):
                result.append('B')
                break
            elif a[1:a[0] + 1].count(f) == b[1:b[0] + 1].count(f):
                result.append('D')
                break
        else:
            if a[1:a[0] + 1].count(f) > b[1:b[0] + 1].count(f):
                result.append('A')
                break
            elif a[1:a[0] + 1].count(f) < b[1:b[0] + 1].count(f):
                result.append('B')
                break

print(*result, sep='\n')
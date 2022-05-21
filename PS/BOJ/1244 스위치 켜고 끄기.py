#1boy 2girl
import sys

N = int(sys.stdin.readline())
switch = list(map(int, sys.stdin.readline().split()))
switch.insert(0, 0)
M = int(sys.stdin.readline())
student = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

for s in student:
    if s[0] == 1: #boy
        n, i = s[1], 1
        while n*i < len(switch):
            switch[n*i] = (1 if switch[n*i] == 0 else 0)
            i += 1
    elif s[0] == 2:
        n, i = s[1], 0
        while True:
            if switch[n-i] == switch[n+i]:
                i += 1
                if n+i >= len(switch) or n-1 <= 0:
                    i -= 1
                    break
            else:
                i -= 1
                break
        for c in range(n-i, n+i+1):
            switch[c] = (1 if switch[c] ==0  else 0)
del switch[0]


result = ' '.join(map(str, switch))
for i in range(0, len(result), 40):
    print(result[i:i+40])


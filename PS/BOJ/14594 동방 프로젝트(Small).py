
#union-find algorithm

def find(x):
    if parent[x] != x:
        return find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b :
        parent[b] = a
    else:
        parent[a] = b


N = int(input())
M = int(input())
smash = [list(map(int, input().split())) for _ in range(M)]
parent = [0] * (N + 1)
for i in range(1, N+1):
    parent[i] = i

for i in range(M):
    s, e = smash[i]
    for j in range(s+1, e+1):
        union(s, j)

group = set()
for i in range(1, N+1):
    group.add(find(i))
print(len(group))
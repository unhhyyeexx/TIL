
def find(x):
    if parent[x] != x:
        return find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    parent = [0] * (N+1)
    for i in range(1, N+1):
        parent[i] = i

    tmp = list(map(int, input().split()))
    for i in range(M):
        union(tmp[2*i], tmp[2*i + 1])

    unionset =set()
    for i in range(1, N+1):
        unionset.add(find(i))

    print(f'#{t+1} {len(unionset)}')


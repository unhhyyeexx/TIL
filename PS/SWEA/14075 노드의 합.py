def sumnode(center):
    if center > N:
        return 0
    if tree[center] == 0:
        tree[center] = sumnode(center*2) + sumnode(center*2 + 1)
        return tree[center]
    else:
        return tree[center]


T = int(input())
for t in range(T):
    N, M, L = map(int, input().split())
    tree = [0]*(N+1)
    for m in range(M):
        node, value = map(int, input().split())
        tree[node] = value
    sumnode(1)
    print(f'#{t+1} {tree[L]}')


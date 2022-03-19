from collections import deque
def binarysearchtree(node):
    if node > N:
        return
    #루트의 왼쪽 노드는 현재노드의 두배. 제일 아래 제일 왼쪽노드(value=1)까지 재귀
    binarysearchtree(node * 2)
    tree[node] = value.popleft()
    #루트의 오른쪽 노드는 현재노드의 두배 +1.
    binarysearchtree(node*2 + 1)


T = int(input())
for t in range(T):
    N = int(input())
    tree = [0]*(N+1)
    value = deque(list(range(1,N+1)))
    binarysearchtree(1)

    print(f'#{t+1} {tree[1]} {tree[N//2]}')
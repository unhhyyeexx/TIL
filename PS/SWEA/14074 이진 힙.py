import heapq
#heapify로 했더니 안돼요,, 왜지..?
def f(node):
    if node == 0:
        return 0
    else:
        return f(node//2) + heap[node-1]


T = int(input())
for t in range(T):
    N = int(input())
    heap = []
    for i in list(map(int, input().split())):
        heapq.heappush(heap, i)
    result = f(N) - heap[N-1]
    print(f'#{t+1} {result}')

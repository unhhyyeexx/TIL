
def subtree(node):
    global answer
    for sub in child[node]:
        subtree(sub)
    answer += 1


T = int(input())
for t in range(T):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    child = [[] for _ in range(E+2)]
    for i in range(0,E*2,2):
        child[arr[i]].append(arr[i+1])

    answer = 0
    subtree(N)
    print(f'#{t+1} {answer}')

def f(node):
    oper = ['+', '-', '*', '/']
    if tree[node] not in oper:
        return tree[node]
    left = child[node][0]
    right = child[node][1]
    if tree[node] == '+':
        return f(left) + f(right)
    elif tree[node] == '-':
        return f(left) - f(right)
    elif tree[node] == '*':
        return f(left) * f(right)
    elif tree[node] == '/':
        return f(left) / f(right)


T = 10
for t in range(T):
    N = int(input())
    tree = [0] * (N + 1)
    child = [[] for _ in range(N + 1)]
    for n in range(N):
        tmp = list(input().split())
        if len(tmp) == 4:
            tree[int(tmp[0])] = tmp[1]
            child[int(tmp[0])].append(int(tmp[2]))
            child[int(tmp[0])].append(int(tmp[3]))
        elif len(tmp) == 2:
            tree[int(tmp[0])] = int(tmp[1])

    result = int(f(1))
    print(f'#{t + 1} {result}')

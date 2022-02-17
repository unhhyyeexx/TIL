T = int(input())
for t in range(T):
    alpa = set(input())
    text = input()

    check = dict()
    for a in alpa:
        if not check.get(a):
            check[a] = 0
    for tt in text:
        if tt in check:
            check[tt] += 1
    result = max(check.values())
    print(f'#{t+1} {result}')



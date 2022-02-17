T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    text = [input() for _ in range(N)]
    trans = []
    for i in range(N):
        temp = ''
        for j in range(N):
            temp += text[j][i]
        trans.append(temp)

    for i in range(N):
        for j in range(N-M+1):
            if text[i][j:j+M] == text[i][j:j+M][::-1]:
                result = text[i][j:j+M]
            if trans[i][j:j+M] == trans[i][j:j+M][::-1]:
                result = trans[i][j:j+M]

    print(f'#{t+1} {result}')
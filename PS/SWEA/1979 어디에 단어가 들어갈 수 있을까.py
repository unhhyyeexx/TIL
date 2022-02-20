def one_count(lst, size, length):
    cnt = 0
    for n in range(size):
        one = 0
        for i in range(size):
            if lst[n][i] == 1:
                one += 1
            else:
                if one == length:
                    cnt += 1
                one = 0
        if one == length:
            cnt += 1
    return cnt

T = int(input())
for t in range(T):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    trans = []
    for i in range(N):
        temp = []
        for j in range(N):
            temp.append(puzzle[j][i])
        trans.append(temp)

    p_cnt = one_count(puzzle, N, K)
    t_cnt = one_count(trans, N, K)

    print(f'#{t+1} {p_cnt+t_cnt}')


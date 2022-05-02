def solution(board, moves):
    answer = 0
    n= len(board)
    transs = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            transs[j][i] = board[i][j]
    trans = []
    for t in transs:
        t.reverse()
        trans.append(t)
    for t in trans:
        while True:
            if t[-1] != 0: break
            else : t.pop()

    stack = []
    cnt = 0
    for m in moves:
        if trans[m-1]:
            stack.append(trans[m-1].pop())
            if len(stack)>=2 and stack[-1] == stack[-2]:
                del stack[-1]
                del stack[-1]
                cnt += 2
    answer = cnt
    return answer
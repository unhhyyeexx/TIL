T = int(input())
for t in range(T):
    sudoku = [list(map(int, input().split())) for _ in range(9)]

    trans, box = [], []
    for i in range(9):
        t_temp = []
        for j in range(9):
            t_temp.append(sudoku[j][i])
        trans.append(t_temp)

    for i in range(0,9,3):
        for j in range(0,9,3):
            tmp = []
            tmp += sudoku[j][i:i+3]
            tmp += sudoku[j+1][i:i + 3]
            tmp += sudoku[j+2][i:i + 3]
            box.append(tmp)

    result = 1
    for i in range(9):
        for c in range(1,10):
            if sudoku[i].count(c) != 1 or trans[i].count(c) != 1 or box[i].count(c) != 1:
                result = 0
                break
    print(f'#{t+1} {result}')
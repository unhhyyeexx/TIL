
def solution(row):
    global cnt
    if row == N:
        cnt += 1
        return
    for c in range(N):
        if col[c] or dia1[c-row] or dia2[c+row]:
            continue
        col[c], dia1[c-row], dia2[c+row] = 1, 1, 1
        solution(row + 1)
        col[c], dia1[c - row], dia2[c + row] = 0, 0, 0

T = int(input())
for t in range(T):
    N = int(input())
    cnt = 0
    #가로, 우상향대각선, 우하향대각선
    col, dia1, dia2 = [0]*N, [0] * (2*N-1), [0] * (2*N-1)
    solution(0)

    print(f'#{t+1} {cnt}')

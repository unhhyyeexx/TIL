
password = {
    "0001101" : 0,
    "0011001" : 1,
    "0010011" : 2,
    "0111101" : 3,
    "0100011" : 4,
    "0110001" : 5,
    "0101111" : 6,
    "0111011" : 7,
    "0110111" : 8,
    "0001011" : 9
}

def findrc(N,M):
    for n in range(N):
        for m in range(M-1, 0, -1):
            if lst[n][m]:
                rc = [n, m]
                return rc


T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    answer = 0
    lst = [list(map(int, input())) for _ in range(N)]

    rc = findrc(N, M)
    row, column = rc[0], rc[1]

    origin = lst[row][column-55 : column+1]
    eigen = []
    for i in range(0, 56, 7):
        tmp = ''
        for j in range(7):
            tmp += str(origin[i+j])
        eigen.append(password[tmp])

    odd, even = 0, 0
    for e in range(7):
        if e % 2:
            even += eigen[e]
        else:
            odd += eigen[e]
    sumvalue = odd*3 + even + eigen[-1]
    if sumvalue % 10 == 0:
        answer += sum(eigen)

    print(f'#{t+1} {answer}')
    

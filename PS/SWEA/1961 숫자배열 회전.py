def rotate(orig_matrix, size):
    rot_matrix = [[0]*size for _ in range(N)]
    for i in range(size):
        for j in range(size):
            rot_matrix[i][j] = orig_matrix[size-1-j][i]
    return rot_matrix

T = int(input())
for t in range(T):
    N = int(input())
    origin  = [list(input().split()) for _ in range(N)]

    quater1 = rotate(origin, N)
    half = rotate(quater1, N)
    quater3 = rotate(half, N)

    print(f'#{t+1}')
    for i in range(N):
        print(''.join(quater1[i]), ''.join(half[i]), ''.join(quater3[i]))


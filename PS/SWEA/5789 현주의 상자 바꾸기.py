#N 박스 개수, Q 숫자를 바꾸는 횟수
T = int(input())
for t in range(T):
    N, Q = map(int, input().split())
    box = [0 for _ in range(N)]
    for q in range(1,Q+1):
        start, end = map(int, input().split())
        box[start-1:end] = [q]*(end-start+1)
    print(f'#{t+1} {" ".join(map(str, box))}')


def solution(alst, blst):
    global answer
    for b in blst:
        l, r = 0, N-1
        pre = ''
        while l<=r:
            mid = (l+r) // 2
            if b == alst[mid]:
                answer += 1
                break
            elif b > alst[mid]: #should go right
                if pre == 'r':
                    break
                else:
                    l = mid + 1
                    pre = 'r'
            else: #should go left
                if pre == 'l':
                    break
                else:
                    r = mid - 1
                    pre = 'l'


T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))
    answer = 0
    solution(A, B)

    print(f'#{t+1} {answer}')

def solution(n):
    answer = ''
    i = 1
    while n:
        if n >= 2 ** ((-1) * i):
            answer += '1'
            n -= 2 ** ((-1) * i)
            i += 1
        else:
            answer += '0'
            i += 1
        if len(answer) >= 13:
            return 'overflow'
    return answer

T = int(input())
for t in range(T):
    N = float(input())
    result = solution(N)
    print(f'#{t+1} {result}')

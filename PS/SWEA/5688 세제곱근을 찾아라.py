
def f(n):
    for i in range(n+1):
        if i**3 == n:
            return i
        elif i**3 > n:
            return -1

T = int(input())
for t in range(T):
    N = int(input())
    result = f(N)
    print(f'#{t+1} {result}')


def solution(lst):
    if len(lst) <= 1:
        return lst

    pivot = lst[0]
    tail = lst[1:]

    left = [x for x in tail if x <= pivot]
    right = [x for x in tail if x > pivot]

    return solution(left) + [pivot] + solution(right)


T = int(input())
for t in range(T):
    N = int(input())
    ai = list(map(int, input().split()))
    result = solution(ai)

    print(f'#{t+1} {result[N//2]}')

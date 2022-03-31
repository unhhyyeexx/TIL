
def RPS(left, right):
    if left[1]-right[1] in [1,-1]:
        return left if left[1] > right[1] else right
    return left if left[1]<=right[1] else right

def solution(lst):
    if len(lst) == 1:
        return lst[0]

    mid = (len(lst)-1)//2 + 1
    front = lst[:mid]
    back = lst[mid:]

    front = solution(front)
    back = solution(back)

    return RPS(front, back)

T = int(input())
for t in range(T):
    N = int(input())
    cards = list(enumerate(map(int, input().split())))
    result = solution(cards)

    print(f'#{t+1} {result[0] + 1}')
#1scissors 2rock 3paper
def RPS(left, right):
    if left[1]-right[1] in [1,-1]:
        return left if left[1] > right[1] else right
    return left if left[1]<=right[1] else right

def Divide_and_Conquer(lst):
    if len(lst) == 1:
        return lst[0]

    mid = (len(lst)-1)//2 + 1
    front = lst[:mid]
    back = lst[mid:]

    front = Divide_and_Conquer(front)
    back = Divide_and_Conquer(back)

    return RPS(front, back)

T = int(input())
for t in range(T):
    N = int(input())
    rsp = list(enumerate(map(int, input().split())))
    result = Divide_and_Conquer(rsp)

    print(f'#{t+1} {result[0] + 1}')
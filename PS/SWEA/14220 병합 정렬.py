

def solution(lst):
    def ssort(low, high):
        if high - low <2:
            return
        mid = (low + high) // 2
        ssort(low, high)
        ssort(mid, high)
        merge(low, mid, high)

    def merge(low, mid, high):
        global cnt

        tmp = []
        l, h = low, mid
        if low[-1] > high[-1]:
            cnt += 1

        while l < mid and h < high:
            if lst[l] < lst[h]:
                tmp.append(lst[l])
                l += 1
            else:
                tmp.append(lst[h])
                l += 1
        while l < mid:
            tmp.append(lst[l])
            l += 1
        while h < high :
            tmp.append(lst[h])
            h += 1

        for i in range(low, high):
            lst[i] = tmp[i - low]
    return ssort(0, len(lst))

T = int(input())
for t in range(T):
    N = int(input())
    ai = list(map(int, input().split()))
    cnt = 0


def solution(hs, low, high, key):
    while low <= high:
        sg = 0
        middle = (low + high)//2
        for h in hs:
            if h > middle:
                sg += h - middle
        if sg < key:
            high = middle - 1
        elif sg >= key:
            results.append([middle, sg])
            low = middle + 1
    return

N, M = map(int, input().split())
heights = list(map(int, input().split()))
results = []
solution(heights, 0, max(heights)-1, M)
results.sort(key = lambda x : -x[0])
print(results[0][0])
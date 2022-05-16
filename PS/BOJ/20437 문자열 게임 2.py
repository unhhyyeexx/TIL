
def solution(words, k):
    result = []

    check = dict()
    for w in words:
        if w not in check:
            check[w] = [1, 1]
        else:
            if check[w][0] == k:
                result.append(check[w])
                del result[w]
            else:
                check[w][0] += 1
        for c in check:
            check[c][1] += 1
    if result:
        maxv = max(result)
        minv = min(result)
        print(minv, maxv)
    else:
        print(-1)

T = int(input())
for t in range(T):
    W = input()
    K = int(input())
    solution(W, K)

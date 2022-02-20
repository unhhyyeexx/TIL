def howmuch(prices, length):
    margin = 0
    idx = length - 1
    while idx > 0:
        for i in range(idx - 1, -1, -1):
            if prices[idx] > prices[i]:
                margin += prices[idx] - prices[i]
            else:
                idx = i
                break
        else:
            break
    return margin


T = int(input())
for t in range(T):
    N = int(input())
    price = list(map(int, input().split()))
    result = howmuch(price, N)

    print(f'#{t + 1} {result}')


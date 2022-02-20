T = int(input())
for t in range(T):
    n = int(input())
    prices1 = input()
    prices = [int(i) for i in reversed(prices1.split(' '))]
    maxvalue = 0
    sumvalue = 0
    for i in prices:
        if maxvalue < i:
            maxvalue = i
        sumvalue += maxvalue - i

    print(f'#{t + 1} {sumvalue}')
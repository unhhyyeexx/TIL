#테케 하나가 다섯줄
T = int(input())
for t in range(T):
    five = [list(input()) for _ in range(5)]
    maxlen = 0
    for f in five:
        if len(f) > maxlen: maxlen = len(f)
    result = ''
    for idx in range(maxlen):
        for one in five:
            if len(one) >= idx+1:
                result += one[idx]
    print(f'#{t+1} {result}')
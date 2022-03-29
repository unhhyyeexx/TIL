
def solution(lst, now):
    if lst[now] >= 3:
        return 1
    if lst[now-2] and lst[now-1] and lst[now]:
        return 1
    if now <= 8 and lst[now-1] and lst[now+1] and lst[now]:
        return 1
    if now <= 7 and lst[now+2] and lst[now+1] and lst[now]:
        return 1

    return 0


T = int(input())
for t in range(T):
    cards = list(map(int, input().split()))
    result = 0

    #p1, p2의 카드 중 같은 카드 개수
    p1 = [0] * 10
    p2 = [0] * 10

    for i in range(12):
        if i % 2:
            p2[cards[i]] += 1
            if solution(p2, cards[i]):
                result = 2
                break
        else:
            p1[cards[i]] += 1
            if solution(p1, cards[i]):
                result = 1
                break
    print(f'#{t+1} {result}')
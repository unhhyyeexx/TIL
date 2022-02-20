# 2,3,5,7,11로만 소인수분해가 되는 숫자들(문제조건)

T = int(input())
for t in range(T):
    num = int(input())
    factor = {2:0, 3:0, 5:0, 7:0, 11:0}
    for key in factor:
        while num % key == 0:
            num //= key
            factor[key] += 1
    print(f'#{t + 1} {" ".join(map(str, factor.values()))}')

bdic = {1 : 0, 0 : 1}
tdic = {0 : [1, 2], 1 : [0, 2], 2 : [0, 1]}

def BinToDec(b):
    b = b[::-1]
    d = 0
    for i in range(len(b)):
        d += (2 ** i) * b[i]
    return d

def TerToDec(t):
    t = t[::-1]
    d = 0
    for i in range(len(t)):
        d += (3 ** i) * t[i]
    return d

T = int(input())
for tc in range(T):
    answer = 0
    binary = list(map(int, input()))
    ternary = list(map(int, input()))

    blst = []
    for bi in range(len(binary)):
        tmp = binary[bi]
        binary[bi] = bdic[binary[bi]]
        blst.append(BinToDec(binary))
        binary[bi] = tmp

    for te in range(len(ternary)):
        if answer :
            break
        tmp = ternary[te]
        for j in range(2):
            ternary[te] = tdic[ternary[te]][j]
            ttmp = TerToDec(ternary)
            if ttmp in blst:
                answer = ttmp
                break
            ternary[te] = tmp

    print(f'#{tc + 1} {answer}')
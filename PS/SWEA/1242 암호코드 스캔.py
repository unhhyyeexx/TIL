password = {
    "211" : 0, "221" : 1, "122" : 2, "411" : 3,
    "132" : 4, "231" : 5, "114" : 6, "312" : 7,
    "213" : 8, "112" : 9
}

hextobin = {'0':'0000', '1':'0001', '2':'0010', '3':'0011',
            '4':'0100', '5':'0101', '6':'0110', '7':'0111',
            '8':'1000', '9':'1001', 'A':'1010', 'B':'1011',
            'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111'}

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    maps = list(set([input().strip() for _ in range(N)]))
    answer = 0

    bins = [''] * len(maps)
    for i in range(len(maps)):
        for j in range(M):
            bins[i] += hextobin[maps[i][j]]
        bins[i] = bins[i].rstrip('0')

    check = []
    for i in range(len(maps)):
        zero1, one1, zero2, one2 = 0, 0, 0, 0
        dec = []
        for j in range(len(bins[i])-1, -1, -1):
            if bins[i][j] == '1' and zero2 == 0 and one1 == 0:
                one2 += 1
            elif bins[i][j] == '0' and one1 == 0 and one2>0:
                zero2 += 1
            elif bins[i][j] == '1' and zero1 == 0 and one2>0 and zero2>0:
                one1 += 1
            elif bins[i][j] == '0' and one1>0 and zero2>0 and one2>0:
                minv = min(one1, zero2, one2)
                tmp = str(one1//minv) + str(zero2//minv) + str(one2//minv)
                dec.append(password[tmp])
                one2 = zero2 = one1 = 0

            if len(dec) == 8:
                dec = dec[::-1]
                odd, even = 0, 0
                for n in range(7):
                    if n % 2:
                        even += dec[n]
                    else:
                        odd += dec[n]
                sumvalue = odd * 3 + even + dec[-1]
                if sumvalue % 10 == 0 and dec not in check:
                    answer += sum(dec)
                check.append(dec)
                dec = []

    print(f'#{t+1} {answer}')



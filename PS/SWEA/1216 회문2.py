T = 10
c = 100
for t in range(T):
    N = int(input())
    lsts = [input() for _ in range(c)]
    #transpose
    transs = [[0]*c for _ in range(c)]
    trans =[]
    for i in range(c):
        temp = ''
        for j in range(c):
            temp += lsts[j][i]
        trans.append(temp)

    maxlen = 1
    for i in range(c): #100줄
        minl, maxl = 0, c
        #제일 큰 길이부터 검사 -> 시간줄이기 위해
        for length in range(maxl, minl, -1):
            #현재 찾은 최대길이 회문보다 길이가 작으면 검사 안해도 됨
            if maxlen >= length :
                break
            for start in range(c-length+1):
                if lsts[i][start:length+start] == lsts[i][start:length+start][::-1]:
                    if maxlen < length:
                        maxlen = length
                if trans[i][start:length+start] == trans[i][start:length+start][::-1]:
                    if maxlen < length:
                        maxlen = length
    print(f'#{t+1} {maxlen}')
def solution(dartResult):
    answer = 0
    score = []
    origin = ''
    sdt = {'S':1, 'D':2, 'T':3}
    for d in dartResult:
        if d in list(sdt.keys()):
            score.append(int(origin)**sdt[d])
            origin = ''
        elif d == '*':
            tmp = []
            i = 0
            while score and i<2:
                tmp.append(score.pop() * 2)
                i+= 1
            score += reversed(tmp)
        elif d == '#':
            tmp = score.pop()
            score.append(tmp * (-1))
        else:
            origin += d

    answer = sum(score)

    return answer
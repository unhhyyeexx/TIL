#Boyer-Moore Algorithm
def skip(pattern, char):
    for i in range(len(pattern)-2, -1, -1):
        if pattern[i] == char:
            return len(pattern)-i-1
    return len(pattern)

def boyer(pattern, text, move):
    cnt = 0
    patternlen = len(pattern)
    textlen = len(text)
    i = 0
    while i <= textlen - patternlen:
        j = patternlen - 1
        while j >= 0:
            if pattern[j] != text[i+j]:
                move = skip(pattern, text[i + patternlen - 1])
                break
            j = j - 1
        if j == -1:
            cnt += 1
            i += 1
        else:
            i += move
    return cnt


T = int(input())
for t in range(T):
    text, pattern = input().split()
    p_cnt = boyer(pattern, text)
    result = p_cnt + (len(text) - (len(pattern) * p_cnt))
    print(f'#{t+1} {result}')


    i=0
    for p in pattern:
        if not check.get(p):
            check[p] = i
            i += 1
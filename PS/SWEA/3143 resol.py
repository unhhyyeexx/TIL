# Boyer-Moore Algorithm

def boyer(pattern, text):
    cnt = 0
    patternlen = len(pattern)
    textlen = len(text)
    i = 0
    while i <= textlen - patternlen:
        j = patternlen - 1
        while j >= 0:
            if pattern[j] != text[i+j]:
                move = len(pattern) if pattern_dit.get(text[i + patternlen - 1]) == None else pattern_dit.get(text[i + patternlen - 1])
                break
            j = j - 1
        if j == -1:
            cnt += 1
            i += len(pattern)
        else:
            i += move
    return cnt


T = int(input())
for t in range(T):
    text, pattern = input().split()

    pattern_dit = {pattern[i]: len(pattern) - i-1 for i in range(len(pattern)-1)}

    p_cnt = boyer(pattern, text)
    result = p_cnt + (len(text) - (len(pattern) * p_cnt))
    print(f'#{t+1} {result}')
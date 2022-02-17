#BoyerMooer algorithm
#불필요한 탐색 스킵
def skip(pattern, char):
    for i in range(len(pattern)-2, -1, -1):
        if pattern[i] == char:
            return len(pattern)-i-1
    return len(pattern)
#BM 본 함수
#text안에 pattern과 일치하는 문자열 있으면 1반환 바로 종료
#끝까지 탐색했는데 pattern과 일치하는 문자열이 없으면 0반환
def boyer(pattern, text):
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
            return 1
        else:
            i += move
    return 0


T = int(input())
for t in range(T):
    pattern = input()
    text = input()
    result = boyer(pattern, text)
    print(f'#{t+1} {result}')
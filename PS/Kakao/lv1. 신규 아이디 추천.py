from string import ascii_lowercase


def solution(new_id):
    answer = ''
    # 1. 소문자
    new_id = new_id.lower()

    # 2. 특수기호 제거(except -, _, .)
    new = ''
    allow = list(ascii_lowercase) + ['_', '-', '.'] + ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    for i in new_id:
        if i in allow: new += i
    new_id = new

    # 3. 마침표 두 번 이상이면 하나로 치환
    while '..' in new_id:
        new_id = new_id.replace('..', '.')

    # 4. 마침표 처음 끝 제거
    new_id = new_id.rstrip('.')
    new_id = new_id.lstrip('.')

    # 5. 빈문자열이면 a대입
    if new_id == '': new_id = 'a'

    # 6. 길이가 16자 이상이면 15자까지만 살리고 다 제거, 마침표가 끝에 위치하면 마침표도 제거
    if len(new_id) >= 16:
        new_id = new_id[:15]
    new_id = new_id.rstrip('.')

    # 7. 길이가 2자 이하면 길이가 3이 될때까지 마지막 글자 붙이기
    while len(new_id) <= 2:
        new_id += new_id[-1]
    answer = new_id

    return answer
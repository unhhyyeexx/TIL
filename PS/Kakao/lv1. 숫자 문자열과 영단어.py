def solution(s):
    answer = 0
    english = {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9', 'zero':'0'}
    for e in list(english.keys()):
        s = s.replace(e, english[e])
    answer = int(s)

    return answer
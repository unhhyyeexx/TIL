answer = 0


def dfs(numbers, target, sumvalue, d):
    global answer

    l = len(numbers)
    if d == l:
        if sumvalue == target:
            answer += 1
        return
    sumvalue_p = sumvalue + numbers[d]
    sumvalue_m = sumvalue - numbers[d]
    dfs(numbers, target, sumvalue_p, d + 1)
    dfs(numbers, target, sumvalue_m, d + 1)


def solution(numbers, target):
    global answer
    answer = 0
    dfs(numbers, target, 0, 0)

    return answer
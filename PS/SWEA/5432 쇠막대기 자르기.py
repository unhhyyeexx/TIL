T = int(input())
for t in range(T):
    brackets = list(input())
    stack = []
    result = 0
    for i in range(len(brackets)):
        if brackets[i] == '(':
            stack.append(brackets[i])

        elif brackets[i] == ')':
            if brackets[i - 1] == '(':  # 레이저위치라면
                del stack[-1]
                result += len(stack)

            else:  # bar의 끝부분
                del stack[-1]
                result += 1
    print(f'#{t+1} {result}')

T = int(input())

for tc in range(T):
    text = input()

    stack = []
    for t in text:
        if len(stack) == 0:
            stack.append(t)
        else:
            if t == stack[-1]:
                stack.pop()
            else:
                stack.append(t)
    print(f'#{tc+1} {len(stack)}')
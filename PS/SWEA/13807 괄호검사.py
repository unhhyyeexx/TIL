def bracket(sentence):
    front = ['(', '{']
    back = [')', '}']
    stack = []
    for s in sentence:
        if s in front:
            stack.append(s)
        elif s in back:
            if len(stack) == 0:
                return 0
            for i in range(2):
                if s == back[i]:
                    if stack[-1] == front[i]:
                        stack.pop()
                    else:
                        return 0
    if stack: return 0
    else: return 1


T = int(input())


for tc in range(T):
    text = input()
    result  = bracket(text)
    print(f'#{tc+1} {result}')




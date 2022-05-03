
text = list(input())
bomb = list(input())

stack = []
for t in text:
    stack.append(t)
    if stack[len(stack)-len(bomb):] == bomb:
        for i in range(len(bomb)):
            stack.pop()

result = ''
if not stack:
    result = 'FRULA'
else:
    result = "".join(stack)

print(result)
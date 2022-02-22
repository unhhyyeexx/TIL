#N=40일 때 경우의 수 11
#10,20,30,40,50 일 때를 다 보면 수열형태로 표현가능
#i번째 답을 구하려면 (i-1)값 + 2*(i-2)값 -> 10, 20일 때는 그냥 선언,,,

def papercnt(width):
    w = width//10
    stack = []
    for i in range(1,w+1):
        if i == 1: stack.append(1)
        elif i == 2: stack.append(3)
        else:
            stack.append(stack[-1] + (2*stack[-2]))
    return stack[-1]

T = int(input())
for t in range(T):
    N = int(input())
    result = papercnt(N)
    print(f'#{t+1} {result}')

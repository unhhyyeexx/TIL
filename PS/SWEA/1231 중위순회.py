

#중위순회 : 왼쪽-루트-오른쪽
def inorder(root):
    global char
    if root:
        inorder(left[root])
        char += tree[root]
        inorder(right[root])



T = 10
for t in range(T):
    N = int(input())
    left = [0]*(N+1)
    right = [0]*(N+1)
    tree = [0] * (N+1)
    for n in range(N):
        one = input().split()
        tree[int(one[0])] = one[1]
        if len(one) == 4:
            left[int(one[0])] = int(int(one[2]))
            right[int(one[0])] = int(int(one[3]))
        elif len(one) == 3:
            left[int(one[0])] = int(int(one[2]))
    char = ''
    inorder(1)
    print(f'#{t+1} {char}')




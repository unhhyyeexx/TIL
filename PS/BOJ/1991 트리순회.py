#동빈나 강의 참고

#전위순회 : 루트-왼쪽-오른쪽
def preorder(root):
    print(root, end='')
    if tree[root][0] != '.':
        preorder(tree[root][0])
    if tree[root][1] != '.':
        preorder(tree[root][1])

#중위순회 : 왼쪽-루트-오른쪽
def inorder(root):
    if tree[root][0] != '.':
        inorder(tree[root][0])
    print(root, end='')
    if tree[root][1] != '.':
        inorder(tree[root][1])

#후위순회 : 왼쪽-오른쪽-루트
def postorder(root):
    if tree[root][0] != '.':
        postorder(tree[root][0])
    if tree[root][1] != '.':
        postorder(tree[root][1])
    print(root, end='')

N = int(input())
tree = {}
for n in range(N):
    center, left, right = input().split()
    tree[center] = [left, right]

preorder('A')
print()
inorder('A')
print()
postorder('A')

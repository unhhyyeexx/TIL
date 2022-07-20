
# 처음에 방 전부 1로 초기화
# 방 부실 때마다 방 0으로 바꿔줌

N = int(input())
M = int(input())
parent = [1] * (N+1)
for _ in range(M):
    s, e = map(int, input().split())
    parent[s:e] = [0]*(e-s)
result = parent.count(1) - 1
print(result)

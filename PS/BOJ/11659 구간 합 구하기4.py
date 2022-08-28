# 누적합

n, m = map(int, input().split())
prearr = list(map(int, input().split()))
arr = [0]
tmp = 0
for i in prearr:
    tmp += i
    arr.append(tmp)

for _ in range(m):
    i, j = map(int, input().split())
    print(arr[j] - arr[i-1])
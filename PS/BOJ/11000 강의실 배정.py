import heapq
import sys # sys모듈 안쓰고 input쓰면 타임에러

N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
arr.sort()

queue = [0]
for i in range(N):
    if queue[0] <= arr[i][0]:
        heapq.heappop(queue)
    heapq.heappush(queue, arr[i][1])

print(len(queue))


# 시간초과
# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
# arr = sorted(arr, key=lambda x:(x[1], x[0]))
# cnt = 0
# while arr:
#     new = arr[:]
#     arr = []
#     end = 0
#     for i in range(len(new)):
#         s, e = new[i][0], new[i][1]
#         if s >= end:
#             end = e
#         else:
#             arr.append(new[i])
#     cnt += 1
# print(cnt)

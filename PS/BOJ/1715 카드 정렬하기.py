# 그리디
# 우선순위 큐

import sys
import heapq
input = sys.stdin.readline

def solution(n, nums):
    answer = 0
    if n == 1:
        answer = 0
        return answer
    while len(nums)-1:
        tmp = heapq.heappop(nums) + heapq.heappop(nums)
        answer += tmp
        heapq.heappush(nums, tmp)
    return answer

n = int(input())
nums = []
for _ in range(n):
    heapq.heappush(nums, int(input()))

print(solution(n, nums))

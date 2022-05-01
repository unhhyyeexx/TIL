
from itertools import combinations

def solution(n):
    if n >= 1024:
        return -1
    decrease = []
    for i in range(1, 11):
        for c in combinations(range(0, 10), i):
            c = list(c)
            c.sort(reverse=True)
            decrease.append(int("".join(map(str, c))))
    decrease.sort()
    return decrease[n-1]

N = int(input())
print(solution(N))










# timeover
# def is_dec(arr):
#     for i in range(1, len(arr)):
#         if arr[i] >= arr[i-1]:
#             return 1
#     return 0
#
# N = int(input())
# decresce = []
# num = 0
# while True:
#     if N >= 1024:
#         decresce.append(-1)
#         break
#     if len(decresce) == N:
#         break
#     if num < 10:
#         decresce.append(num)
#         num += 1
#         continue
#     arr = list(str(num))
#     if is_dec(arr) == 0:
#         decresce.append(num)
#     num += 1
#
#
# print(decresce[-1])




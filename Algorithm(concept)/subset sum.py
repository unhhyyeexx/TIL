# arr = [3,6,7,1,5,4]
#
# n = len(arr)
#
# for i in range(1<<n):
#     for j in range(n):
#         if i & (1<<j):
#             print(arr[j], end=" ")
#     print()
# print()

#practice2
#10개의 정수를 입력받아 부분집합의 합이 0이 되는 것이 존재하는지를 계산하는 함수 구현
def zerosum(arr):
    n= len(arr)
    for i in range(1<<n):
        subset = []
        for j in range(n):
            if i &(1<<j):
                subset.append(arr[j])
        if subset:
            subset_sum = 0
            for s in subset:
                subset_sum += s
            if subset_sum == 0:
                return True
    return False

nums = list(map(int, input().split()))
print('exist zerosum') if zerosum(nums) else print('no exist zerosum')
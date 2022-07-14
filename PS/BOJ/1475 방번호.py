# 구현
# 220714

def solution(array):
    nums = {'6':0}
    for n in array:
        if n in ['6', '9']:
            nums['6'] += 1
        elif n in nums:
            nums[n] += 1
        else:
            nums[n] = 1

    if nums['6'] % 2 :
        nums['6'] = nums['6']//2 + 1
    else:
        nums['6'] = nums['6']//2

    answer = max(nums.values())
    return answer

number = list(input())
print(solution(number))

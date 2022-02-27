#0~9숫자 카드
#카드 6장 뽑기
# 3장 카드 동일한 번호 triple, 3장카드 연속적인 번호면 run
#run과 triplet으로만 구성된 경우가 baby-gin
#정렬 먼저 필요

def sort(nums):
    for i in range(len(nums)-1, 0, -1):
        for j in range(0, i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

def run(nums):
    for three in range(0, 6, 3):
        for i in range(2):
            if nums[three + i] != nums[three + i +1] -1:
                return False
    return True

def triplet(nums):
    ans = False
    for three in range(0, 6, 3):
        for i in range(2):
            if nums[three + i] == nums[three + i +1]:
                ans = True


numbers = list(map(int, input()))
sortnum = sort(numbers)
result = True if run(sortnum) and triplet(sortnum) else False
print(result)



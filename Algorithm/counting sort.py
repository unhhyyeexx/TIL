
def counting(nums, k):

    #원소들의 개수를 셀 빈 리스트를 만들어 준다.
    #아예 없는 숫자가 있을 수도 있으니 0으로 초기화를 시켜준다.
    cntarr = [0] * (k+1)

    #전체 리스트를 돌면서 각 숫자의 개수를 세어준다.
    #각 숫자를 인덱스로 따져서 cntarr의 원소 += 1
    for num in nums:
        cntarr[num] += 1

    for i in range(1, len((cntarr))):
        cntarr[i] += cntarr[i-1]

    #정렬된 결과가 담길 리스트를 초기화.
    #0~k가 아닌 값으로 초기화 하는 것이 오류를 확인하기 좋음
    resultarr = [-1] * len(nums)

    #오른쪽 -> 왼쪽의 흐름을 왼쪽 -> 오른쪽 흐름으로 가져오기 위해 리스트를 뒤집음
    nums = nums[::-1]

    for i in nums:
        cntarr[i] -= 1
        resultarr[cntarr[i]] = i

    return resultarr

     





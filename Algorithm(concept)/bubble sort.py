def bubble(nums):

    #3. 오른쪽 끝을 나타내는 i가 n-1부터 1까지 이동
    for i in range(len(nums)-1, 0, -1):

        #1. indes j가 0부터 i까지 이동
        for j in range(0, i):

            #2. nums의 j번째 원소가 바로 오른쪽 원소보다 크면 위치 change
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

num =
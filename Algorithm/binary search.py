#이진 탐색을 수행하기 위해서는 자료가 정렬된 상태여야 한다.
#1. 중앙에 있는 원소를 고른다
#2. 중앙 원소의 값과 찾고자 하는 목표 값을 비교
#3.목표 값이 중앙 원소의 값보다 작으면 자료의 왼쪽 반에 대해서, 크다면 자교의 오른쪽 반에 대해서 새로 검색 수행
#4.찾고자 하는 값을 찾을 때까지 과정 반복
#자료에 삽입이나 삭제가 발생했을때 배열의 상태를 항상 정렬 상태로 유지하는 추가 작업 필요

def binary_search(arr, key):
    n = len(arr)
    start, end = 0, n-1
    while start <= end:
        middle = (start+end)//2
        if arr[middle] == key:
            return True
            #searching for idx : return middle
        elif arr[middle] > key:
            end = middle -1
        elif arr[middle] < key:
            start = middle + 1
    return False


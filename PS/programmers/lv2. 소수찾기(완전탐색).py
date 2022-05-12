
from itertools import permutations
import math

def primenum(number):
    if number < 2:
        return False
    # 제곱근 값을 기준으로 양옆 약수의 개수가 같음 => 한쪽만 조사해도 됨
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

def solution(numbers):
    prime = set()
    for n in range(1, len(numbers)+1):
        perm = list(map(''.join, permutations(numbers, n)))
        for p in list(set(perm)):
            if primenum(int(p)):
                prime.add(int(p))

    answer = len(prime)
    return answer

appeach = '17'
frodo = solution(appeach)
print(frodo)
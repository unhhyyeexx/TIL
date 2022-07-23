
from itertools import combinations

n, m = map(int, input().split())

answer = list(combinations(range(1, n+1), m))
for a in answer:
    print(*a)
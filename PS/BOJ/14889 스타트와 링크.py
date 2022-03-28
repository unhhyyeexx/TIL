from itertools import combinations
N = int(input())
people = list(range(N))
graph = []
for n in range(N):
    graph.append(list(map(int, input().split())))

combis = combinations(people, N//2)
answer = 1e9

for s in combis:
    l = list(set(people) - set(s))
    start, link = 0, 0
    sc = combinations(s, 2)
    lc = combinations(l, 2)
    for ts in sc:
        start += graph[ts[0]][ts[1]]
        start += graph[ts[1]][ts[0]]
    for tl in lc:
        link += graph[tl[0]][tl[1]]
        link += graph[tl[1]][tl[0]]
    answer = min(answer, abs(start - link))
print(answer)


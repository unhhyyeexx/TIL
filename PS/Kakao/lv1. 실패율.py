def solution(N, stages):
    answer = []
    people = len(stages)
    rate = dict()
    for i in range(1, N + 1):
        rate[i] = 0
        if people != 0:
            rate[i] = stages.count(i) / people
            people -= stages.count(i)

    answer = list(map(lambda x: x[0], reversed(sorted(rate.items(), key=lambda x: (x[1], -x[0])))))

    return answer
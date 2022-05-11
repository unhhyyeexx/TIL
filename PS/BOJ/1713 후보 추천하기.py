
def solution():
    # 학생 추천수 배열
    students = [0] * (max(rec) + 1)
    # 사진 [누구, 언제] 배열
    photo = [[0,0] for _ in range(N)]
    n = 0
    while [0,0] in photo and n<=N:
        student = rec[n]
        students[student] += 1
        for p in photo:
            if p[0] == student:
                n += 1
                break
        else:
            idx = photo.index([0,0])
            photo[idx][0] = student
            photo[idx][1] = n
            n += 1
    for m in range(n, M):
        for p in photo:
            if p[0] == rec[m]:
                students[rec[m]] += 1
                break
        else:
            student = rec[m]
            students[student] += 1
            minv = sorted(photo, key=lambda x:(students[x[0]], x[1]))[0]
            minstu = minv[0]
            minidx = photo.index(minv)
            students[minstu] = 0
            photo[minidx][0] = rec[m]
            photo[minidx][1] = m
    answer = []
    for p in photo:
        if p[0]!= 0:
            answer.append(p[0])
    return answer

N = int(input())
M = int(input())
rec = list(map(int, input().split()))
result = sorted(solution())
if result:
    print(' '.join(map(str, result)))




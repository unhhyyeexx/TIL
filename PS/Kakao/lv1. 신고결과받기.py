def solution(id_list, report, k):
    answer = [0] * len(id_list)

    # 신고당한 횟수를 셀 dict
    # key : id_list, value: 일단 0
    reported_cnt = dict()
    for id in id_list:
        reported_cnt[id] = 0

    # 신고당한 횟수만큼 += 1
    for r in set(report):
        reported_cnt[r.split()[1]] += 1

    # 신고당한 횟수가 k번을 넘는 사용자 선택
    # 그 사용자를 신고한 사람들한테 answer에서 += 1
    for r in set(report):
        if reported_cnt[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer
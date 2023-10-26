def solution(priorities, location):
    answer = 0
    ans_dic = {}
    idx_p = [x for x in range(1, len(priorities)+1)] # 실행 순서 (1부터)
    loc = [x for x in range(len(priorities))] # 처음 위치 (0부터)

    while priorities:
        if priorities[0] == max(priorities):
            ans_dic[loc[0]] = idx_p[0]
            priorities.pop(0)
            idx_p.pop(0)
            loc.pop(0)

        else:
            p = priorities.pop(0)
            priorities.append(p)
            lo = loc.pop(0)
            loc.append(lo)

    answer = ans_dic[location]
    return answer
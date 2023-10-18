def solution(clothes):
    answer = 1
    dic = {}
    lst = []
    case = 1
    for i in clothes:
        lst.append(i[1])
    for j in lst:
        if j in dic:
            dic[j] += 1
        else:
            dic[j] = 1
    for count in dic.values():
        answer *= (count + 1)
    
    return answer - 1
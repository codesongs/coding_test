def solution(arr):
    answer = []
    for i in arr:
        if not answer or i != answer[-1]:  # 불일치시 저장
            answer.append(i)
    return answer
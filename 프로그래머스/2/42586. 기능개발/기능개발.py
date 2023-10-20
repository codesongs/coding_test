def solution(progresses, speeds):
    answer = []
    
    while progresses: # 작업이 남아있는 경우        
        for idx, speed in enumerate(speeds):
            progresses[idx] += speed           
        i = 0
        
        while progresses and progresses[0] >= 100: # 첫 작업 진행률 100 이상
            del progresses[0], speeds[0] # 작업 삭제
            i += 1
            
        if i > 0:
            answer.append(i)
    
    return answer


# 날짜 i 라고 가정
# progresses에 speeds를 더한다 
# progresses[0] 이 100 이상이면 삭제
# 100 미만이면 다시 i=0으로 두고 처음부터 수행



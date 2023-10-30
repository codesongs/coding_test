import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)  # 힙으로 변형
    min_heap = scoville

    while min_heap[0] < K:    
        min1 = heapq.heappop(min_heap)
        min2 = heapq.heappop(min_heap)
        new = min1 + min2 * 2
        heapq.heappush(min_heap, new)
        answer += 1

        if len(min_heap) == 2 and (min_heap[0]+2*min_heap[1]) < K:
            return -1

    return answer
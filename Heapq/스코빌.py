import heapq



def solution(scoville, K):
    
    answer = 0
    heapq.heapify(scoville)
    operation =0
    
    
    while scoville:
        
        min = heapq.heappop(scoville)
        if min >= K:
            return operation
        # print(min)
        if not scoville:
            return -1
        min2 = heapq.heappop(scoville)
        
        new = (min + min2*2)
        heapq.heappush(scoville, new)
        operation +=1
        
    return -1
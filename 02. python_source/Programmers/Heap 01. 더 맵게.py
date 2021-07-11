# 2021.07.09

# 내 풀이 (Heap 사용 안해서 시간 초과)
def solution(scoville, K):
    cnt = 0
    finished = False
    
    while finished == False:
        scoville.sort()
        
        if scoville[0] >= K:
            finished = True            
        
        else:
            new = scoville[0] + scoville[1]*2
            del scoville[0:2]
            scoville.append(new)
            cnt += 1
            if len(scoville) == 1:
                cnt = -1
                finished = True
        
    
    return cnt


# Heap 사용 풀이
import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    i = 0
    while scoville[0] < K:
        if len(scoville) > 1:
            heapq.heappush(scoville, heapq.heappop(scoville) + (heapq.heappop(scoville)*2))
            i += 1
        else:
            return -1
    return i
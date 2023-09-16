import heapq as hp

def solution(scoville, K):
    hp.heapify(scoville)    # scoville 리스트를 힙 자료형으로 만들기
    
    count = 0
    while scoville[0] < K :
        count += 1
        
        min_one = hp.heappop(scoville)
        min_two = hp.heappop(scoville)
        hp.heappush(scoville, min_one + min_two*2)
        
        # 모든 스코빌을 K 이상으로 만들 수 없는 경우
        if (len(scoville) == 2) and (scoville[0] + scoville[1]*2) < K:
            return -1
        
    return count


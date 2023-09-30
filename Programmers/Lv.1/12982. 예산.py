def solution(d, budget):
    minus = 0
    count = len(d)
    
    # 아무런 예산도 지원해줄 수 없는 경우를 예외처리 -> 테스트 3에 대한 에러 해결!
    if min(d) > budget: return 0
    
    for i in sorted(d, reverse=True):
        if sum(d)-minus <= budget:
            return count
        else:
            minus += i
            count -= 1

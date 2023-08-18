def solution(N, stages):
    player = len(stages)
    fail_ratio = {}
    
    for i in range(1, N+1):
        # 스테이지에 남은 사용자 수가 0이 아닐 때
        if player != 0:
            fail_ratio[i] = stages.count(i) / player
            player -= stages.count(i)
       
        # 스테이지에 남은 사용자 수가 0일 때
        else:
            fail_ratio[i] = 0

    return sorted(fail_ratio, key=lambda x: fail_ratio[x], reverse=True)

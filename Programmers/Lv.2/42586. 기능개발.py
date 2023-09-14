import math

def solution(progresses, speeds):
    answer = []
    
    # time 리스트에 몇일 후 배포가 가능한지를 담음
    time = []
    for progress, speed in zip(progresses, speeds):
        time.append(math.ceil((100-progress) / speed))
    
    # 배포 시간을 앞과 비교하며, 최종 반환 리스트에 값을 추가하기
    count = 1
    before = time[0]
    for i in range(1, len(time)):
        if before < time[i]:   # 이전 작업시간이 먼저 끝날 때
            answer.append(count)
            count = 1
            before = time[i]
        else:                  # 이전 작업시간이 현 작업시간보다 오래걸릴 때
            count += 1
    answer.append(count)
    
    return answer

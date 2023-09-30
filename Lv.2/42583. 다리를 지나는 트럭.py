from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    truck = deque(truck_weights)                        # 트럭이 대기하는 deque
    bridge = deque([0 for _ in range(bridge_length)])   # 다리 길이 만큼의 deque

    w = 0
    while True:
        answer += 1     # 시간이 1 증가
        
        bridgeOut = bridge.popleft()
        w -= bridgeOut

        # 새로 올라와야 하는 트럭의 무게가 weight보다 큰 경우 -> 트럭이 올라오지 못함
        if w+truck[0] > weight:
            bridge.append(0)
            
        # 새로 올라와야 하는 트럭의 무게가 weight보다 큰 경우 -> 트럭이 올라오지 못함
        else:
            w += truck[0]
            bridge.append(truck[0])
            truck.popleft()
            
        # 모든 트럭이 전부 통과한 경우
        if len(truck) == 0:
            answer += len(bridge)
            return answer

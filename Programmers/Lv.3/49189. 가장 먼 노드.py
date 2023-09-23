from collections import deque

def solution(n, vertex):
    # 연결된 노드 딕셔너리 형태로 만들기
    graph = {i+1: [] for i in range(n)}
    for v in vertex:
        graph[v[0]].append(v[1])
        graph[v[1]].append(v[0])
    
    # BFS(Breadth-First Search) 활용 탐색하기
    queue = deque([1])                      # 1을 큐에 삽입하고 시작
    distance = [0 for _ in range(n)]        # 노드 1과 얼마나 떨어져 있는지를 구하기 위함
    while queue:
        lq = queue.popleft()
        for i in graph[lq]:
            if distance[i-1] == 0:                   # 거리가 0이란 뜻은 아직 방문하지 않았다는 뜻임
                distance[i-1] = distance[lq-1] + 1   # 누적거리를 추가 (예, 노드 6의 경우 노드 3보다 하나 더 멈)
                queue.append(i)
                
    return distance[1:].count(max(distance[1:]))     # 거리가 가장 먼 값들의 카운트

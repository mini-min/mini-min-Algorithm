def solution(n):
    answer = []
    graph = []
    max_num = 0     # 집어넣을 값의 범위
    
    # 그래프 세팅과, max_num값 구하는 반복문
    for i in range(n):
        graph.append([])
        max_num += i+1
        
    arrow = 0   # 화살표 방향 (0은 아래, 1은 오른쪽, 2는 위)
    
    row = 0     # 값을 넣을 행 인덱스
    col = 0     # 값을 넣을 열 인덱스

    fill = n        # 얼마나 이동해야하는지를 알려주는 카운트
    check_fill = 0  # 얼마나 이동했는지를 비교하는 카운트
        
    # max_num 만큼 반복하면서 리스트 위치에 따라 값을 넣어주기
    for i in range(max_num):
        
        # arrow 0: 밑으로 내려가면서 값을 채우는 화살표 방향
        if arrow == 0:
            graph[row].insert(col, i+1)   # 아래부터 순서대로 가장 앞에 넣기
            check_fill += 1               # 1 이동함
            
            # 아직 내려갈 위치가 남은 경우
            if check_fill < fill:
                row += 1
                
            # 아래로 내려가서 가장 바닥을 찍은 경우
            elif check_fill == fill:
                fill -= 1        # 이동해야 하는 범위는 1 마이너스.
                check_fill = 0   # 얼마 이동했는지를 알려주는 카운트는 다시 초기화
                arrow = 1        # 화살표 방향을 바꿈
                col += 1         # 오른쪽으로 한칸 이동해야함

        # arrow 1: 오른쪽으로 가면서 값을 채우는 화살표 방향
        elif arrow == 1:
            graph[row].insert(col+check_fill, i+1)    # 오른쪽순대로 값을 넣기
            check_fill += 1     # 1 이동함
            
            # 오른쪽으로 이동을 다 한 경우
            if check_fill == fill:
                fill -= 1       # 이동해야 하는 범위는 1 마이너스
                check_fill = 0  # 얼마 이동했는지를 알려주는 카운트는 다시 초기화
                row -= 1    # 위로 올라가야하므로, row를 1 줄인다.
                arrow = 2   # 화살표 방향을 바꿈

        # arrow 2: 위로 올라가면서 값을 채우는 화살표 방향
        elif arrow == 2:
            graph[row].insert(col, i+1)   #
            check_fill += 1     # 1 이동함
            
            # 아직 올라갈 위치가 남은 경우
            if check_fill < fill:
                row -= 1
                
            # 위로 올라가서 가장 윗 부분을 찍은 경우
            elif check_fill == fill:
                fill -= 1       # 이동해야 하는 범위는 1 마이너스
                check_fill = 0  # 얼마 이동했는지를 알려주는 카운트는 다시 초기화
                row += 1    # 밑으로 내려가야하므로, row를 1 증가시켜준다.
                arrow = 0   # 화살표 방향을 바꿈
                
    # graph 리스트를 벗기고, 반환을 위한 하나의 answer 리스트에 새로 담는다
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            answer.append(graph[i][j])

    return answer

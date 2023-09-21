def solution(priorities, location):
    double_priorities = priorities * len(priorities)
    queue = sorted(priorities)   # 우선순위를 꺼내기 위해 정렬된 priorities 리스트
    count = 0                    # 반환용 실행순서
    idx = len(queue)-1           # 현재 가장 높은 우선순위를 담고 있는 인덱스
    high_prior = queue[idx]      # 가장 높은 우선순위

    for i, q in enumerate(double_priorities):
        # 대기중인 프로세스가 가장 높은 우선순위와 일치할 때
        if q == high_prior:
            count += 1           # 실행 1 증가
            
            idx -= 1
            high_prior = queue[idx]

            # 내가 알고 싶었던 위치의 프로세스가 꺼내졌을 때
            if i%len(priorities) == location:
                return count

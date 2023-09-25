"""
아직 미 해결
def solution(n, results):
    answer = 0
    grid = [[0 for _ in range(n)] for _ in range(n)]    # 기본 그리드 세팅
    
    # 이긴 경우에는 1을 추가, 진 경우에는 -1을 추가
    for a, b in results:
        grid[a-1][b-1] = 1
        grid[b-1][a-1] = -1
        print(grid)
                    
    answers=[0 for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if grid[i-1][j-1]==1:
                answers[i-1]+=1
                answers[j-1]+=1
    for i in range(n):
        if answers[i-1]==n-1:
            answer+=1
    return answer
"""

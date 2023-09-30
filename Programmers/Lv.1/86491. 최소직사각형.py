def solution(sizes):
    max_width = max_height = 0
    
    # 모든 명함의 가로 길이와 세로 길이를 순회
    for size in sizes:
        width, height = size
        max_width = max(max_width, width, height)
       
    # 현재 명함의 가로 길이와 세로 길이 중에서 최소값을 최대 세로 길이로 갱신
        max_height = max(max_height, min(width, height))
   
    # 최대 가로 길이와 최대 세로 길이를 곱하여 최소 크기의 지갑을 반환
    return max_width * max_height

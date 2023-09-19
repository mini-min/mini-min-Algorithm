def solution(t, p):
    answer = 0
    part_list = [int(t[i:i+len(p)]) for i in range(len(t)-len(p)+1)]
    
    for num in part_list:
        if int(p) >= num:
            answer += 1
    return answer

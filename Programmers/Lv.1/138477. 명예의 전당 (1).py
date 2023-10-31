def solution(k, score):
    answer = []
    legend_score = []
    
    for s in score:
        if len(legend_score) == k:
            if legend_score[0] < s:
                del legend_score[0]
            
        if len(legend_score) < k:
            legend_score.append(s)
            legend_score.sort()
        
        answer.append(legend_score[0])
    
    return answer

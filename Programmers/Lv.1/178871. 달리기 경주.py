def solution(id_list, report, k):    
    # 처리 결과 메일이 갈 횟수 -> 최종 return 리스트
    answer = [0] * len(id_list)
    
    # 신고당한 카운트를 체크할 리스트
    check_dic = {x: 0 for x in id_list}
    
    # 중복 리스트 제거, 리포트를 반복하면서 신고당한 횟수 체크
    for ch in [r.split(" ") for r in set(report)]:
        check_dic[ch[1]] += 1
        
    # 중복 리스트 제거, 리포트를 반복하면서 신고 횟수가 k 이상인 유저를 신고한 경우에 answer 카운트를 증가
    for ch in [r.split(" ") for r in set(report)]:
        if check_dic[ch[1]] >= k:
            answer[id_list.index(ch[0])] += 1        
            
    return answer


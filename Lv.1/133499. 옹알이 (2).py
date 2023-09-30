def solution(babbling):
    answer = 0
    for bb in babbling:
        for b in ["aya", "ye", "woo", "ma"]:
            # 연속해서 같은 발음이 있는 경우를 제외하기 위한 조건 추가
            if b*2 not in bb: bb = bb.replace(b, "0")

        # 최종적으로 남아있는 단어가 0으로만 구성되어 있으면, 최종 반환값을 1 추가함.
        if bb.isdigit(): answer += 1
        
    return answer

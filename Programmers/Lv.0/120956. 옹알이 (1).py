def solution(babbling):
    answer = 0
    can_babbling = ["aya", "ye", "woo", "ma"]
    
    for sp in babbling:
        for can_sp in can_babbling:
            sp = sp.replace(can_sp, "0")

        if sp.isdigit(): answer += 1
        
    return answer

# 1. 특이한 정렬
def solution(numlist, n):
    chlist = [abs(num-n-0.1) for num in numlist]
    answer = []
    
    for _ in range(len(chlist)):
        answer.append(numlist[chlist.index(min(chlist))])
        chlist[chlist.index(min(chlist))] = 10001
    return answer
    
# 2. 등수 매기기
def solution(score):
    avg = [sum(num)/2 for num in score]
    sort_avg = sorted(avg, reverse=True)
    answer = []
    
    for num in avg:
        answer.append(sort_avg.index(num)+1)
    
    return answer
    
# 3. 옹알이 (1)
def solution(babbling):
    answer = 0
    can_babbling = ["aya", "ye", "woo", "ma"]
    
    for sp in babbling:
        for can_sp in can_babbling:
            sp = sp.replace(can_sp, "0")

        if sp.isdigit(): answer += 1
        
    return answer
    
# 4. 로그인 성공?
def solution(id_pw, db):
    for check in db:
        if check[0] == id_pw[0]:
            if check[1] == id_pw[1]: return "login"
            else: return "wrong pw"
    return "fail"

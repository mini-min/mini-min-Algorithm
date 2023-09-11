def solution(clothes):
    hash_dict = {}
    answer = 1
    
    # 딕셔너리 값에 추가하기
    for cloth in clothes:
        if cloth[1] in hash_dict:
            hash_dict[cloth[1]].append(cloth[0])
        else:
            hash_dict[cloth[1]] = [cloth[0]]

    # 조합 찾기
    for dic in hash_dict:
        if len(hash_dict)==1:   # 조합 종류가 하나인 경우 -> 이 안에서 return
            return len(hash_dict[dic])
        else:                   # 조합 종류가 여러개인 경우
            answer *= len(hash_dict[dic])+1
    return answer-1             # 조합 종류가 여러개인 경우 -> 곱셈 연산 이후 값을 return


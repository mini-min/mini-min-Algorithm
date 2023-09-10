def solution(s):
    answer = ""     # 최종 답안으로 반환할 문자열
    count = 0       # 단어별로 인덱스를 체크하기 위한 카운트

    for i in range(len(s)):
        if count%2 == 0:    # 단어별로 구분한 인덱스가 짝수인 경우 -> upper()
            answer += s[i].upper()
        else:               # 단어별로 구분한 인덱스가 홀수인 경우 -> lower()
            answer += s[i].lower()
        
        count += 1          # 단어의 인덱스를 1 증가 시킴

        """만약, 반복시킨 문자열이 공백인 경우 -> 단어를 구분해야하므로, 인덱스 카운트를 초기화한다."""
        if s[i] == " ":
            count = 0
            
    return answer

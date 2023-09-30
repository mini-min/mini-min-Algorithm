def solution(n):
    answer = n+1                            # n보다 하나 큰 수부터 비교시작
    one_count = str(bin(n)[2:]).count("1")  # n을 2진수로 변환했을 때의 1의 개수
    while True:
        # n 2진수 1의 개수와 answer 1의 개수가 같으면 반환
        if one_count == str(bin(answer)).count("1"):
            return answer
        # 1의 개수가 다르다면 answer를 1 증가
        else:
            answer += 1
            
            
"""
다른 사람의 풀이
def nextBigNumber(n):
    num1 = bin(n).count('1')    # 나처럼 문자열로 변환하지 않고도, 2진수 자체 카운트를 사용할 수 있다.
    while True:
        n = n + 1
        if num1 == bin(n).count('1'):
            break
    return n
"""

# 1. 숫자 찾기
def solution(num, k):
    answer = str(num).find(str(k))

    if answer == -1: return answer
    else: return answer+1
    
# 2. n의 배수 고르기
def solution(n, numlist):
    return [i for i in numlist if i%n==0]
    
# 3. 자릿수 더하기
def solution(n):
    answer = 0
    while n != 0:
        answer += n % 10
        n //= 10
    return answer
    
# 4. OX퀴즈
def solution(quiz):
    answer = []
    for q in quiz:
        if str(eval(q[:q.find("=")])) == q[q.find("=")+2:]: answer += "O"
        else: answer += "X"
    return answer

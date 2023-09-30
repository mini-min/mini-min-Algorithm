# 내 코드
# 약수 갯수를 구하는 함수
def count_divisor(num):
    count = 0
    for i in range(1, num+1):
        if num % i == 0: count += 1
    return count
    
# 문제 구하는 함수
def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        if count_divisor(i) % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer

"""
다른 사람의 풀이 (참고)
def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        # 약수가 홀수개인 모든 수는 제곱수이다.
        # 즉, 루트를 했을 때 정수가 된다면 빼기를, 그 조건이 아니라면 더하기를 해줄 수 있다.
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer
"""

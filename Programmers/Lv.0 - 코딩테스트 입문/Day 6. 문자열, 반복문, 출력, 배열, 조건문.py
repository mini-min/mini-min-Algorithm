# 1. 문자열 뒤집기
def solution(my_string):
    return my_string[::-1]
    
# 2. 직각삼각형 출력하기
n = int(input())
for i in range(1, n+1):
    print("*"*i)
    
# 3. 짝수 홀수 개수
def solution(num_list):
    answer = [0, 0]
    for i in num_list:
        answer[i%2] += 1
    return answer
    
# 4. 문자 반복 출력하기
def solution(my_string, n):
    return ''.join(i*n for i in my_string)

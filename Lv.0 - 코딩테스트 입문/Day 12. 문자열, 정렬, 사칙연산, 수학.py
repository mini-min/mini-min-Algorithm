# 1. 모음 제거
def solution(my_string):
    return "".join([i for i in my_string if not(i in "aeiou")])
    
# 2. 문자열 정렬하기 (1)
def solution(my_string):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    answer = [int(i) for i in my_string if i not in alpha]
    return sorted(answer)
    
# 3. 숨어있는 숫자의 덧셈 (1)
def solution(my_string):
    return sum(int(i) for i in my_string if i.isdigit())
    
# 4. 소인수분해
def find_prime(n):
    for i in range(2, n):
        if n % i == 0: return False
    return True

def solution(n):
    answer = [i for i in range(2, n+1) if n % i == 0 and find_prime(i)]

    return answer

# 1. 문자열안에 문자열
def solution(str1, str2):
    return 1 if str2 in str1 else 2
    
# 2. 제곱수 판별하기
import math

def solution(n):
    return 1 if math.sqrt(n) == int(math.sqrt(n)) else 2
    
# 3. 세균 증식
def solution(n, t):
    while t!=0:
        n*=2
        t-=1
    return n
    
# 4. 문자열 정렬하기 (2)
def solution(my_string):
    return "".join(sorted(my_string.lower()))

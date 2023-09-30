# 1. 편지
def solution(message):
    return len(message)*2
    
# 2. 가장 큰 수 찾기
def solution(array):
    return [max(array), array.index(max(array))]
    
# 3. 문자열 계산하기
def solution(my_string):
    return sum(int(i) for i in my_string.replace(' - ', ' + -').split(' + '))
    
# 4. 배열의 유사도
def solution(s1, s2):
    return len(set(s1)&set(s2))

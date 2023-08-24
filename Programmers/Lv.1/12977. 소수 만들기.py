# 소수 판별 함수
def is_sosu(num):
    for i in range(2, num):
        if num % i == 0: return False
    return True

# 문제 풀이 부분
from itertools import combinations
def solution(nums):
    answer = 0
    for i in combinations(nums, 3):
        if is_sosu(sum(i)):
            answer += 1
    return answer

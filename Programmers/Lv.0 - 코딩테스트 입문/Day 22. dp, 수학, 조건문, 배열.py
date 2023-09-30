# 1. 저주의 숫자 3
def solution(n):
    answer = 0
    while n > 0:
        while str(answer).count('3') != 0 or answer % 3 == 0:
            answer += 1
        answer += 1
        n -= 1
    return answer-1
    
# 2. 평행
def solution(dots):
    if (dots[0][1]-dots[1][1])/(dots[0][0]-dots[1][0]) == (dots[2][1]-dots[3][1])/(dots[2][0]-dots[3][0]): return 1
    elif (dots[0][1]-dots[2][1])/(dots[0][0]-dots[2][0]) == (dots[1][1]-dots[3][1])/(dots[1][0]-dots[3][0]): return 1
    elif (dots[0][1]-dots[3][1])/(dots[0][0]-dots[3][0]) == (dots[1][1]-dots[2][1])/(dots[1][0]-dots[2][0]): return 1
    else: return 0
    
# 3. 겹치는 선분의 길이
def solution(lines):
    answer = 0
    line1 = list(range(lines[0][0], lines[0][1]+1))
    line2 = list(range(lines[1][0], lines[1][1]+1))
    line3 = list(range(lines[2][0], lines[2][1]+1))
    
    if len(list(set(line1) & set(line2)))==0:
        answer += 0
    else:
        answer += len(list(set(line1) & set(line2)))-1
    
    if len(list(set(line2) & set(line3)))==0:
        answer += 0
    else:
        answer += len(list(set(line2) & set(line3)))-1
    
    if len(list(set(line1) & set(line3)))==0:
        answer += 0
    else:
        answer += len(list(set(line1) & set(line3)))-1
    
    if len(list(set(line1) & set(line2) & set(line3)))==0:
        answer += 0
    else:
        answer -= (len(list(set(line1) & set(line2) & set(line3)))-1)*2
        
    return answer
    
# 4. 유한소수 판별하기
import math

def find_prime(n):
    for i in range(2, n):
        if n % i == 0: return False
    return True

def solution(a, b):
    gcd = math.gcd(a, b)
    a, b = a//gcd, b//gcd
    
    check = [num for num in range(2, b+1) if b % num == 0 and find_prime(num)]
    
    for n in check:
        if n == 2 or n == 5: continue
        else: return 2
    return 1

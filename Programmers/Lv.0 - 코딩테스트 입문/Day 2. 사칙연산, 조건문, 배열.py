# 1. 두 수의 나눗셈
def solution(num1, num2):
    return int(num1/num2*1000)
    
# 2. 숫자 비교하기
def solution(num1, num2):
    return 1 if num1==num2 else -1
    
# 3. 분수의 덧셈
import math

def solution(numer1, denom1, numer2, denom2):
    numer3, denom3 = numer1*denom2 + numer2*denom1, denom1 * denom2
    gcd = math.gcd(numer3, denom3)
    
    return [numer3, denom3] if gcd==1 else [numer3/gcd, denom3/gcd]
    
# 4. 배열 두 배 만들기
def solution(numbers):
    return [i*2 for i in numbers]

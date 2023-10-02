# 1. 배열 자르기
def solution(numbers, num1, num2):
    return numbers[num1:num2+1]
    
# 2. 외계행성의 나이
def solution(age):
    new_age = ""
    
    while age!=0:
        new_age+=chr(age%10+97)
        age//=10
    
    return new_age[::-1]
    
# 3. 진료순서 정하기
def solution(emergency):
    s_emergency = sorted(emergency, reverse=True)
    return [s_emergency.index(i)+1 for i in emergency]
    
# 4. 순서쌍의 개수
def solution(n):
    answer = [i for i in range(2, n+1) if n % i == 0]
    return len(answer)+1

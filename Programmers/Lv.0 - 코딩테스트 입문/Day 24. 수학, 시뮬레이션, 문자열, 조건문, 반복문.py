# 1. 치킨 쿠폰
def solution(chicken):
    answer = 0
    
    while chicken >= 10:
        answer += chicken//10
        chicken = chicken//10+chicken%10
    
    return answer
    
# 2. 이진수 더하기
def solution(bin1, bin2):
    num1, num2 = int(bin1, 2), int(bin2, 2)
    answer = bin(num1 + num2)
    return answer[2:]
    
# 3. A로 B 만들기
def solution(before, after):
    return 1 if sorted(before) == sorted(after) else 0
    
# 4. k의 개수
def solution(i, j, k):
    answer = 0
    for num in range(i, j+1):
        answer += str(num).count(str(k))
    return answer

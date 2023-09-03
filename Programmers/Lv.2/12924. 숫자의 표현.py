def solution(n):
    answer = 0
    
    for i in range(n):
        acc_sum = 0

        for j in range(i, n):
            acc_sum += j+1
            if acc_sum == n: answer += 1
            elif acc_sum > n: break
            
    return answer
    
"""
다른 사람의 참고 코드
def expressions(num):
    return len([i for i in range(1, num+1, 2) if num % i is 0])
"""

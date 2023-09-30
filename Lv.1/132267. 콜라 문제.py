def solution(a, b, n):
    answer = 0
    
    while n >= a:
        bott = (n//a)*b
        answer += bott
        n = bott + n%a
    
    return answer

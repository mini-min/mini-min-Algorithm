# 1. 피자 나눠 먹기 (1)
def solution(n):
    if n%7==0: return n/7
    else: return n//7+1
    
# 2. 피자 나눠 먹기 (2)
def solution(n):
    m = 6
    let_n, let_m = n, m

    while n != m:
        if n > m: m+=let_m
        else: n+=let_n

    return n/6
    
# 3. 피자 나눠 먹기 (3)
def solution(slice, n):
    return (n-1)//slice+1
    
# 4. 배열의 평균값
def solution(numbers):
    return sum(numbers)/len(numbers)

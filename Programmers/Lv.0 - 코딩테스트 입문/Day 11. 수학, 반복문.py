# 1. 주사위의 개수
def solution(box, n):
    return (box[0]//n)*(box[1]//n)*(box[2]//n)
    
# 2. 합성수 찾기
def solution(n):
    answer = 0

    for i in range(2, n+1):
        count = 0
        for j in range(1, i+1):
            if i % j == 0: count += 1
        if count >= 3: answer += 1

    return answer
    
# 3. 최댓값 만들기 (1)
def solution(numbers):
    numbers.sort()
    return numbers[-1] * numbers[-2]
    
# 4. 팩토리얼
def solution(n):
    fac = 3628800
    for i in range(10, 0, -1):
        if fac > n: fac //= i
        else: return i

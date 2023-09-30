"""
1차 시도 (런타임 에러)
def solution(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (solution(n-1) + solution(n-2)) % 1234567
"""

def solution(n):
    fibonacci = [0, 1]
    for i in range(2, n):
        fibonacci.append(fibonacci[i-1] + fibonacci[i-2])

    return (fibonacci[n-1]+fibonacci[n-2]) % 1234567

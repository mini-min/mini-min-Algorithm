# 1. 가까운 수
def solution(array, n):
    s_array = sorted(array)
    n_array = [abs(num-n) for num in s_array]
    return s_array[n_array.index(min(n_array))]

# 2. 369 게임
def solution(order):
    count = 0
    for i in str(order):
        if i in "369": count += 1
    return count
    
# 3. 암호 해독
def solution(cipher, code):
    return cipher[code-1::code]
    
# 4. 대문자와 소문자
def solution(my_string):
    return "".join([ch.lower() if ch.isupper() == True else ch.upper() for ch in my_string])

# 1. 영어가 싫어요
def solution(numbers):
    alpha = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    for i in range(len(alpha)):
        if alpha[i] in numbers:
            numbers = numbers.replace(alpha[i], num[i])

    return int(numbers)
    
# 2. 인덱스 바꾸기
def solution(my_string, num1, num2):
    return my_string[:num1] + my_string[num2] + my_string[num1+1:num2] + my_string[num1] + my_string[num2+1:]
    
# 3. 한 번만 등장한 문자
def solution(s):
    set_s = set(s)
    return "".join(sorted([i for i in set_s if s.count(i) == 1]))
    
# 4. 약수 구하기
def solution(n):
    return [i for i in range(1, n+1) if n % i == 0]

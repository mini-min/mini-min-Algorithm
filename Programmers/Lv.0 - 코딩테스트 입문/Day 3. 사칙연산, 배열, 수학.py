# 1. 나머지 구하기
solution = lambda num1, num2: num1%num2

# 2. 중앙값 구하기
def solution(array):
    array.sort()
    return array[len(array)//2]
    
# 3. 최빈값 구하기
import collections

def solution(array):
    answer = collections.Counter(array)
    mode_number = answer.most_common(1)[0][0]
    
    if len(array)==1:
        return mode_number
    else:
        if answer.most_common(2)[0][1] == answer.most_common(2)[1][1]:
            return -1
        else:
            return mode_number

# 4. 짝수는 싫어요
def solution(n):
    return [num for num in range(n+1) if num%2!=0]

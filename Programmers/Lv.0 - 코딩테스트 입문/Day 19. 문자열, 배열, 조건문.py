# 1. 7의 개수
def solution(array):
    return str(array).count('7')
    
# 2. 잘라서 배열로 저장하기
def solution(my_str, n):
    answer = []
    s = ""
    
    for i in my_str:
        if len(s) < n:
            s += i
        else:
            answer.append(s)
            s = ""
            s += i
            
    answer.append(s)
    return answer
    
# 3. 중복된 문자 개수
def solution(array, n):
    return array.count(n)
    
# 4. 머쓱이보다 키 큰 사람
def solution(array, height):
    answer = 0
    for i in array:
        if i > height:
            answer += 1
    return answer

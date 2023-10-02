# 1. 컨트롤 제트
def solution(s):
    lists = s.split(" ")
    indexes = [i-1 for i, c in enumerate(lists) if c == "Z"]

    for num in indexes: lists[num] = ""

    return sum([int(i) for i in lists if i not in "Z"])
    
# 2. 배열 원소의 길이
def solution(strlist):
    return [len(i) for i in strlist]
    
# 3. 중복된 문자 제거
def solution(my_string):
    answer = ""
    for i in my_string:
        if i not in answer: answer += i
    return answer
    
# 4. 삼각형의 완성조건 (1)
def solution(sides):
    sides.sort()
    return 1 if sides[2] < sides[0]+sides[1] else 2

def solution(arr):
    answer = [arr[0]]
    before = arr[0]
    
    for i in arr[1:]:
        if i != before:
            answer.append(i)
            before = i

    return answer

"""
다른 사람의 풀이 코드

def solution(arr):
    result = []
    for c in arr:
        # 인덱싱 -1을 이용하는 코드
        if len(result) == 0 or result[-1] != c:
            result.append(c)

    return result
"""

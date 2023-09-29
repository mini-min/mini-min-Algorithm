def solution(n, arr1, arr2):
    # arr1과 arr2를 비트 연산자 or(|)를 이용해서 하나로 합친다.
    arr_and = [bin(i|j)[2:].zfill(n) for i, j in zip(arr1, arr2)]
    
    # 이진수 값을 "#"와 공백으로 구성된 원래의 값으로 해독한다.
    answer = []
    for i in arr_and:
        ap_string = ""
        for j in i:
            if j == "1": ap_string += "#"
            else: ap_string += " "
        answer.append(ap_string)
    
    return answer
    
"""
다른 사람의 풀이 코드 (참고)
def solution(n, arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        a12 = str(bin(i|j)[2:])
        a12 = a12.rjust(n, '0')
        a12 = a12.replace('1', '#')
        a12 = a12.replace('0', ' ')
        answer.append(a12)
    return answer
"""

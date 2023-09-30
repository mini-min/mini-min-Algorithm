def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        insert_list = []
        for j in range(len(arr1[0])):
            insert_list.append(arr1[i][j] + arr2[i][j])
        answer.append(insert_list)
    return answer

"""
다른 사람의 풀이 코드(참고)
def solution(arr1, arr2):
    answer = [[c + d for c, d in zip(a,b)] for a, b in zip(arr1, arr2)]
    return answer

"""

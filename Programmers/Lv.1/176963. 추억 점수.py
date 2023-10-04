def solution(name, yearning, photo):
    score = {}
    for n, y in zip(name, yearning):
        score[n] = y

    answer = []
    for p in photo:
        longing = 0
        for n in p:
            if n in score:
                longing += score[n]
        answer.append(longing)

    return answer

"""
다른 풀이
1. photo와 photo 안에 있는 내부 리스트를 순서대로 반복
2. (조건) 반복되는 이름이 name 안에 있는 경우
3. name의 인덱스를 찾아 그대로 yearning의 indexing으로 score값을 찾는다.
4. photo 내부 리스트 반복돌 동안의 합계를 리스트에 추가

def solution(name, yearning, photo):
    return [sum(yearning[name.index(j)] for j in i if j in name) for i in photo]
"""

def solution(elements):
    sums = []
    n = len(elements)
    elements = elements*2  # 원형 수열의 느낌을 내기 위해 두배로 이어붙임

    # elements의 반복 시작점
    for i, a in enumerate(elements):
        SUM = a
        sums.append(SUM)

        # 시작점을 기준으로 elements를 슬라이싱해서 원형 수열을 구현하는 느낌
        for b in elements[i+1:i+n]:
            SUM += b
            sums.append(SUM)

    return len(list(set(sums)))

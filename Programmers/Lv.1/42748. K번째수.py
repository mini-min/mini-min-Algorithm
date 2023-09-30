def solution(array, commands):
    # 1. commands 리스트를 반복하면서, array를 슬라이싱한다. -> array[1번째요소-1:2번째 요소]
    # 2. 슬라이싱한 array를 정렬한다. -> sorted()
    # 3. 3번째 반복 요소를 가지고 인덱싱해서 값을 리스트에 추가한다.
    return [sorted(array[cm[0]-1:cm[1]])[cm[2]-1] for cm in commands]

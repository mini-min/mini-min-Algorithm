# 1. 점의 위치 구하기
def solution(dot):
    if dot[0] > 0 and dot[1] > 0:
        return 1
    elif dot[0] < 0 and dot[1] > 0:
        return 2
    elif dot[0] < 0 and dot[1] < 0:
        return 3
    elif dot[0] > 0 and dot[1] < 0:
        return 4
        
# 2. 2차원으로 만들기
def solution(num_list, n):
    out_list, in_list = [], []
    for i in range(len(num_list)):
        in_list.append(num_list[i])
        if len(in_list) == n:
            out_list.append(in_list)
            in_list = []
        
    return out_list
    
# 3. 공 던지기
def solution(numbers, k):
    return numbers[2 * (k - 1) % len(numbers)]
    
# 4. 배열 회전시키기
def solution(numbers, direction):
    if direction == "left":
        numbers.insert(len(numbers), numbers[0])
        del numbers[0]
    else:
        numbers.insert(0, numbers[-1])
        del numbers[-1]
    return numbers

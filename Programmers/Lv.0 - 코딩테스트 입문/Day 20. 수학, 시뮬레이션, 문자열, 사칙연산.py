# 1. 직사각형 넓이 구하기
def solution(dots):
    return (max(dots)[0] - min(dots)[0])*(max(dots)[1] - min(dots)[1])
    
# 2. 캐릭터의 좌표
def solution(keyinput, board):
    answer = [0, 0]
    
    for c in range(len(keyinput)):
        if keyinput[c] == "left" and answer[0] > -(board[0]//2): answer[0] -= 1
        elif keyinput[c] == "right" and answer[0] < (board[0]//2): answer[0] += 1
        elif keyinput[c] == "up" and answer[1] < (board[1]//2): answer[1] += 1
        elif keyinput[c] == "down" and answer[1] > -(board[1]//2): answer[1] -= 1

    return answer
    
# 3. 최댓값 만들기 (2)
def solution(numbers):
    numbers = sorted(numbers)
    return max(numbers[0] * numbers[1], numbers[-1]*numbers[-2])
    
# 4. 다항식 더하기
def solution(polynomial):
    ch, n = [], []
    answer = ""
    
    for num in polynomial.split(" + "):
        if num[-1] == "x":
            if len(num) == 1: ch.append("1")
            else: ch.append(num[:-1])
        else: n.append(int(num))
    
    s_ch = sum((int(x) for x in ch))
    s_n = sum((int(y) for y in n))
    
    if s_ch == 1:
        if s_n == 0: return "x"
        else: return "x + " + str(s_n)
    else:
        if s_ch == 0: return str(s_n)
        elif s_n == 0: return str(s_ch) + "x"
        else: return str(s_ch) + "x + " + str(s_n)

# 1. 숨어있는 숫자의 덧셈 (2)
def solution(my_string):
    num_list = []
    num_string = ""
    answer = 0
    
    for i in my_string:
        if i.isdigit():
            num_string += i
        else:
            num_list.append(num_string)
            num_string = ""
    num_list.append(num_string)  # my_string의 마지막 값이 정수로 끝내는 경우가 있을 수 있음!
    
    for num in num_list:
        if num.isdigit(): answer += int(num)
        
    return answer
    
# 2. 안전지대
def solution(board):
    answer = 0
    
    new_board = []
    for b in board:
        new_board.append(b.copy())
    
    upper, lower, left, right = 0, len(board)-1, 0, len(board[0])-1
    
    for out_ar in range(len(board)):
        for in_ar in range(len(board[0])):
            if new_board[out_ar][in_ar] == 1:
                if out_ar != upper and in_ar != left:
                    board[out_ar-1][in_ar-1] = 1
                if out_ar != upper:
                    board[out_ar-1][in_ar] = 1
                if out_ar != upper and in_ar != right:
                    board[out_ar-1][in_ar+1] = 1
                if in_ar != left:
                    board[out_ar][in_ar-1] = 1
                if in_ar != right:
                    board[out_ar][in_ar+1] = 1
                if out_ar != lower and in_ar != left:
                    board[out_ar+1][in_ar-1] = 1
                if out_ar != lower:
                    board[out_ar+1][in_ar] = 1
                if out_ar != lower and in_ar != right:
                    board[out_ar+1][in_ar+1] = 1
            
    for lst in board:
        answer += lst.count(0)
    return answer
    
# 3. 삼각형의 완성조건 (2)
def solution(sides):
    answer = 0
    sides.append(0)
    
    for i in range(1, sides[0]+sides[1]):
        sides[2] = i
        if max(sides) < (sum(sides)-max(sides)): answer += 1
    
    return answer
    
# 4. 외계어 사전
def solution(spell, dic):
    for i in range(len(dic)):
        r = 0
        for j in spell:
            if j in dic[i]: r += 1
        if r == len(spell): return 1
    return 2

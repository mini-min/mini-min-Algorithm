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
        

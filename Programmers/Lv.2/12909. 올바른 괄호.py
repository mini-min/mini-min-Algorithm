def solution(s):
    open_count = 0
    for gwalho in s:
        if gwalho == "(":
            open_count += 1
        else:
            if open_count == 0: return False
            open_count -= 1
    
    if open_count == 0: return True
    else: return False
    

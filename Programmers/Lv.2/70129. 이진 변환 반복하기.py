def solution(s):
    answer = [0, 0]
    
    def delete_zero(s):
        new_str = ""
        
        if s == "1":
            return answer
        else:
            answer[0] += 1
            for i in s:
                if i != "0": new_str += i
                else: answer[1] += 1
            return delete_zero(bin(int(len(new_str)))[2:])
    
    return delete_zero(s)

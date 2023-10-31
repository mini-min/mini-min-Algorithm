def solution(s):
    int_list = [int(i) for i in s.split(" ")]
    return " ".join([str(min(int_list)), str(max(int_list))])

"""
다른 사람의 풀이 (참고)
def solution(s):
    s = list(map(int,s.split()))
    return str(min(s)) + " " + str(max(s))
"""

def solution(s):
    return "".join(sorted(s, reverse=True))
    lo = ""
    up = ""

    for ch in sorted(s, reverse=True):
        if ch.isupper():
            up += ch
        else:
            lo += ch
            
    return lo + up

"""
다른 사람의 풀이(참고)
def solution(s):
    return ''.join(sorted(s, reverse=True))
"""

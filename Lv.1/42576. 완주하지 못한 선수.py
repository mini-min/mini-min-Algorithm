"""
#1. 런타임 에러 코드
def solution(participant, completion):
    for pl in participant:
        if pl in completion:
            completion.remove(pl)
        else:
            return pl
"""

# 2. sorted 이용 코드 (성공)
def solution(participant, completion):
    participant = sorted(participant)
    completion = sorted(completion)
    
    for i, j in zip(participant, completion):
        if i!=j: return i
    return participant[-1]
    
"""
# 3. 해시 이용 코드 (성공)
def solution(participant, completion):
    hashDict={}
    sumHash=0
    
    for part in participant:
        hashDict[hash(part)]=part
        sumHash+=hash(part)
    
    for comp in completion:
        sumHash-=hash(comp)
        
    return hashDict[sumHash]
"""

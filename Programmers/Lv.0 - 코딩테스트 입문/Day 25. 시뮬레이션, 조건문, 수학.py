# 1. 문자열 밀기
def solution(A, B):
    shift = 1
    if A == B: return 0

    while shift < len(A):
        if A[-shift:]+A[0:-shift] == B:
            return shift
        else:
            shift += 1
    return -1
    
# 2. 종이 자르기
def solution(M, N):
    return (min(M, N)-1)+((max(M, N)-1)*min(M, N))
    
# 3. 연속된 수의 합
def solution(num, total):
    return [(total-sum(range(1, num)))/num+i for i in range(num)]
    
# 4. 다음에 올 숫자
def solution(common):
    if common[1]-common[0] == common[2]-common[1]:
        return common[-1]+(common[1]-common[0])
    else:
        return common[-1]*(common[1]/common[0])

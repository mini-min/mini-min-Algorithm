# 정렬(sorted, sort 모두 사용 가능)의 목적을 정해주는 방법
# key 매개변수와, lambda 식을 함께 사용하면 됨

# 위 문제같은 경우, 인덱스 n의 문자가 같은 문자열이 여러개일 경우, 사전순으로 앞선 문자열이 앞쪽에 위치한다는 조건이 존재
# 사전순으로 먼저 정렬된 리스트를 key=a[n]을 기준으로 다시 정렬시킨다고 문제를 품
# sorted(sorted(strings)) 코드를 사용

def solution(strings, n):
    return sorted(sorted(strings), key=lambda a: a[n])

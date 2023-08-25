# 입력값 받기
num1 = int(input())
num_set = set(map(int, input().split()))        
num2 = int(input())
num_list = list(map(int, input().split()))

# 수 찾기 수행
for num in num_list:
    print(1) if num in num_set else print(0)    # num이 num_set 안에 있으면 1, 없으면 0 출력

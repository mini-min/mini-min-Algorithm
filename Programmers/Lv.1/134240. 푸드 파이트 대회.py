def solution(food):
    answer = ""
    # 1부터 음식별로 나누기 2를 해서 1인당 먹을 수 있는 음식의 양을 저장
    # //2 연산으로, 홀수인 경우 자동 나머지를 처리할 수 있음
    count_food = [food[i]//2 for i in range(1, len(food))]
    
    # count_food를 반복하면서, 인덱스를 음식의 넘버로 count_food 양만큼 곱해서 answer에 추가함
    for i in range(len(count_food)):
        answer += str(i+1)*count_food[i]
    
    # 0을 기준으로 일반 저장값과 슬라이싱을 이용해서 뒤집은 값을 함께 저장함
    return answer + "0" + answer[::-1]

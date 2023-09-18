def solution(prices):
    answer = []
    for i in range(len(prices)):
        count = 1
        for j in range(i+1, len(prices)):
            # 가격이 떨어졌거나, 끝까지 가격이 떨 경우
            if (prices[i] > prices[j]) or (j == len(prices)-1):
                answer.append(count)
                break
            # 가격이 떨어지지 않은 경우
            else:
                count += 1
               
    # 가장 마지막 prices는 절대 가격이 떨어지지 않는다.
    answer.append(0)
    return answer
